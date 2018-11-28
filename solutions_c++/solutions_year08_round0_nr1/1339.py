#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cctype>

using namespace std;

int main(int argc, char *argv[])
{
	int lines;
	std::cin >> lines;

	char sengine[101][101];
	char sword[1001][101];

	int sengine_count;	
	int sword_count;
	char q[101];

	for (int i=0;i<lines;i++) {
		int sengine_count;
		std::cin >> sengine_count;
		
		cin.ignore(1000, '\n');
		for (int j=0;j<sengine_count;j++) {
			cin.getline(sengine[j],256);
			}

		std::cin >> sword_count;
		cin.ignore(1000, '\n');
		for (int j=0;j<sword_count;j++) {
			cin.getline(sword[j],256);
			}

		int res=0;

		for (int j=0;j<sengine_count;j++) 
			q[j]=0;

		for (int j=0;j<sword_count;j++) {
			for (int k=0;k<sengine_count;k++)
				if (strcmp(sengine[k],sword[j])==0) 
					 q[k]=1;
			//printf("%d %d %d %d %d\n",q[0],q[1],q[2],q[3],q[4]);
			char free_q=0;
			for (int k=0;k<sengine_count;k++) 
				if (q[k]==0) free_q=1;
			if (free_q==0) {
		//		printf("switch\n");
				res++;
				for (int l=0;l<sengine_count;l++) 
					q[l]=0;
				for (int k=0;k<sengine_count;k++)
					if (strcmp(sengine[k],sword[j])==0) 
						q[k]=1;

				}
			//printf("%d %s\n",res, sword[j]);
			
		}
		printf("Case #%d: %d\n",i+1,res);
	}
}
