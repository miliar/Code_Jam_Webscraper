#include <cstdlib>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	FILE *in  = fopen("B-small-attempt1.in","r");
	FILE *out = fopen("B-small-attempt1.out","w");
	int tests;
	fscanf(in,"%d",&tests);
	for(int t = 0; t<tests; t++){
		vector< pair<int,int> > hA,hB;
		int ret = 0, turnAround, NA, NB;
		fscanf(in,"%d %d %d",&turnAround,&NA,&NB);

		for(int i = 0; i<NA; i++){
			int hs1,mins1,hs2,mins2;
			fscanf(in,"%d:%d",&hs1,&mins1);
			fscanf(in,"%d:%d",&hs2,&mins2);
			hA.push_back(make_pair(hs1*100+mins1, hs2*100+mins2+turnAround));
		}

		for(int i = 0; i<NB; i++){
			int hs1,mins1,hs2,mins2;
			fscanf(in,"%d:%d",&hs1,&mins1);
			fscanf(in,"%d:%d",&hs2,&mins2);
			hB.push_back(make_pair(hs1*100+mins1, hs2*100+mins2+turnAround));
		}
		
		sort(hA.begin(), hA.end());
		sort(hB.begin(), hB.end());
		
		int A = NA, B = NB;
		vector<bool> used1(102,false);
		for(int i = 0; i<hA.size(); i++)
			for(int j = 0; j<hB.size(); j++)
				if(hA[i].second <= hB[j].first && !used1[j]){
					B--;
					used1[j] = true;
					break;
				}
			

		vector<bool> used2(102,false);
		for(int i = 0; i<hB.size(); i++)
			for(int j = 0; j<hA.size(); j++)
				if(hB[i].second <= hA[j].first && !used2[j]){
					A--;
					used2[j] = true;
					break;
				}

		fprintf(out,"Case #%d: %d %d\n",t+1,A,B);
	}
    return EXIT_SUCCESS;
}
