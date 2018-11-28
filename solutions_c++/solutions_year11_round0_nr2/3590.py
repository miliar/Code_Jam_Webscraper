#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int map[8];
int T,C,D,N;
string comb[37],oppo[29],istr,ostr;

int findmap(char s){
	int res;
	switch(s){
		case 'Q': res = 0; break;
		case 'W': res = 1; break;
		case 'E': res = 2; break;
		case 'R': res = 3; break;
		case 'A': res = 4; break;
		case 'S': res = 5; break;
		case 'D': res = 6; break;
		case 'F': res = 7; break;
		default: res = -1; break;
	}
	return res;
}

bool checkcomb(int p){
	bool res = false;
	int i,a,b,tmp,end;
	if(ostr.empty()) return res;
	end = ostr.size()-1;
	for(i=0;i<C;i++){
		if((comb[i][0]==istr[p]&&comb[i][1]==ostr[end])||(comb[i][1]==istr[p]&&comb[i][0]==ostr[end])){
			tmp = findmap(ostr[end]);
			if(tmp!=-1)
				map[tmp]--;
			ostr[end] = comb[i][2];
			res = true;
			break;
		}
	}	
	return res;
}

bool checkoppo(int p){
	bool res = false;
        int i,a,b,j,tmp;
        for(i=0;i<D;i++){
                if(istr[p]==oppo[i][0]){
			tmp = findmap(oppo[i][1]);
			if(map[tmp]>0){
			ostr.clear();
			for(j=0;j<8;j++)
				map[j]=0;
			res = true;
                        break;}
                }
		else if(istr[p]==oppo[i][1]){
                        tmp = findmap(oppo[i][0]);
                        if(map[tmp]>0){
                        ostr.clear();
                        for(j=0;j<8;j++)
                                map[j]=0;
                        res = true;
                        break;}
                }
        }
        return res;
}

int main(){
	ifstream in;
	in.open("./input2");
	ofstream out;
	out.open("./output2");
	int ncase,i,tmp;
	in>>T;
	for(ncase=1;ncase<=T;ncase++){
		for(i=0;i<8;i++){
			map[i]=0;
		}
		ostr.clear();
		in>>C;
		for(i=0;i<C;i++){
			in>>comb[i];
		}
		in>>D;
		for(i=0;i<D;i++){
			in>>oppo[i];
		}
		in>>N;
		in>>istr;
		ostr.push_back(istr[0]);
		tmp = findmap(istr[0]);
		map[tmp]++;
		for(i=1;i<N;i++){
			if(!checkcomb(i)){
				if(!checkoppo(i)){
				ostr.push_back(istr[i]);
				tmp = findmap(istr[i]);
				map[tmp]++;
				}
			}
		}
		out<<"Case #"<<ncase<<": [";
		int k=ostr.size()-1;
		for(i=0;i<k;i++){
			out<<ostr[i]<<", ";
		}
		if(!ostr.empty())
			out<<ostr[i];
		out<<"]"<<endl;
	}
	in.close();
	out.close();
	return 0;
}
