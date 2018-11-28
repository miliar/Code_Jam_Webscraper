#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class water{
public:
	int W;
	int H;
	int **hmap;
	int **smap;
	char **bmap;

	water():W(0),H(0){
	}

	bool init_map(){
		if(W<1 || H<1)
			return false;
		hmap = new int*[H];
		smap = new int*[H];
		bmap = new char*[H];
		for(int i=0;i<H;i++){
			hmap[i] = new int[W];
			smap[i] = new int[W];
			bmap[i] = new char[W];
			for(int j=0;j<W;j++){
				hmap[i][j] = -1;
				smap[i][j] = -1;
				bmap[i][j] = 'a';
			}
		}
		return true;
	}

	void del_map(){
		for(int i=0;i<H;i++){
			delete [] hmap[i];
			delete [] smap[i];
			delete [] bmap[i];
		}
		delete [] hmap;
		delete [] smap;
		delete [] bmap;
	}

	bool struct_hmap(ifstream& ifs){
		if(!ifs.good())
			return false;
		for(int i=0;i<H;i++){
			for(int j=0;j<W;j++){
				ifs >> hmap[i][j];
			}
		}
	}

	int calc_bmap(){
		vector<pair<int,int>> sink_set;
		vector<pair<int,int>> minb_set;
		vector<pair<int,int>> crs;

		for(int i=0;i<H;i++){
			for(int j=0;j<W;j++){
				if(smap[i][j]>=0)
					continue;
				crs.clear();
				int ci=i, cj=j;
				while(true){
					int minh = hmap[ci][cj];
					int ni=ci, nj=cj;
					if(ci>0){
						//North(-1,0)
						if(hmap[ci-1][cj]<minh){
							minh = hmap[ci-1][cj];
							ni=ci-1;
							nj=cj;
						}
					}
					if(cj>0){
						//West(0,-1)
						if(hmap[ci][cj-1]<minh){
							minh = hmap[ci][cj-1];
							ni=ci;
							nj=cj-1;
						}
					}
					if(cj<W-1){
						//East(0,+1)
						if(hmap[ci][cj+1]<minh){
							minh = hmap[ci][cj+1];
							ni=ci;
							nj=cj+1;
						}
					}
					if(ci<H-1){
						//South(+1,0)
						if(hmap[ci+1][cj]<minh){
							minh = hmap[ci+1][cj];
							ni=ci+1;
							nj=cj;
						}
					}
					if(ci==ni && cj==nj){ //=sink
						sink_set.push_back(pair<int,int>(ci,cj));
						int sind = sink_set.size()-1;
						int mini=ci, minj=cj;
						smap[ci][cj] = sind;
						for(int k=0;k<crs.size();k++){
							smap[crs.at(k).first][crs.at(k).second] = sind;
							if(crs.at(k).first < mini
								|| crs.at(k).first == mini && crs.at(k).second < minj){
									mini = crs.at(k).first;
									minj = crs.at(k).second;
							}
						}
						minb_set.push_back(pair<int,int>(mini,minj));
						break;
					}else if(smap[ni][nj]>=0){ //already reach
						int sind = smap[ni][nj];
						int mini=minb_set.at(sind).first ,minj=minb_set.at(sind).second;
						smap[ci][cj] = sind;
						if(ci < mini || ci == mini && cj < minj){
								mini = ci;
								minj = cj;
						}
						for(int k=0;k<crs.size();k++){
							smap[crs.at(k).first][crs.at(k).second] = sind;
							if(crs.at(k).first < mini
								|| crs.at(k).first == mini && crs.at(k).second < minj){
									mini = crs.at(k).first;
									minj = crs.at(k).second;
							}
						}
						minb_set.at(sind).first = mini;
						minb_set.at(sind).second = minj;
						break;
					}else{
						crs.push_back(pair<int,int>(ci,cj));
						ci = ni;
						cj = nj;
					}
				}
			}
		}
		string abt = "abcdefghijklmnopqrstuvwxyz";
		for(int i=0;i<H;i++){
			for(int j=0;j<W;j++){
				if(smap[i][j]<0 || smap[i][j]>=26)
					return -1;
				bmap[i][j] = abt.at(smap[i][j]);
			}
		}
		return 1;
	}
};
