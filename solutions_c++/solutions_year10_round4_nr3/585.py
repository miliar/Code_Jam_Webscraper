/*
 * C.cpp
 *
 *  Created on: 2010/06/05
 *      Author: jun
 */

#include <stdio.h>
#include <stdlib.h>

#include <map>
#include <vector>

using namespace std;

typedef pair<int,int> ipair;

int main()
{
	int c,C;
	scanf("%d\n",&C);
	for (c=0;c<C;c++){
		map<ipair,int> all_maps;
		int r,R;
		scanf("%d\n",&R);
		int x1,x2,y1,y2;
		for (r=0;r<R;r++){
			scanf("%d %d %d %d\n",&x1,&y1,&x2,&y2);
			int x,y;
			for (x=x1;x<=x2;x++){
				for (y=y1;y<=y2;y++){
					all_maps[ipair(x,y)]=1;
				}
			}
		}
		int sec=0;
		while (all_maps.size()>0){
			vector<ipair> die;
			vector<ipair> born;
			//死滅するバクテリア
			map<ipair,int>::iterator it;
			for (it=all_maps.begin();it!=all_maps.end();it++){
				ipair pos=it->first;
				if (all_maps.find(ipair(pos.first-1,pos.second))==all_maps.end() && all_maps.find(ipair(pos.first,pos.second-1))==all_maps.end()){
					//死ぬ
					die.push_back(pos);
				}
				if (all_maps.find(ipair(pos.first+1,pos.second-1))!=all_maps.end()){
					//生まれる
					born.push_back(ipair(pos.first+1,pos.second));
				}
			}
			int i;
			for (i=0;i<die.size();i++){
				all_maps.erase(die[i]);
			}
			for (i=0;i<born.size();i++){
				all_maps[born[i]]=1;
			}
			sec++;
		}
		printf("Case #%d: %d\n",c+1,sec);
	}
}
