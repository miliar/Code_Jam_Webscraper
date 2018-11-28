#include<iostream>
#include<cstdlib>
#include<string>
#include<vector>
#include<cmath>


using namespace std;

class snap{
	long int N;
	long int K;
public:
	snap(long int _n, long int _k)
	{
		N = _n;
		K = _k;
	}
	bool stateSnap()
	{
		bool state;
		long int a = pow(2.0,N);
		if((K+1)%a == 0)
			state = true;
		else state= false;
		return state;
	}
};

int main()
{
	int n,k;
	int count;
	FILE* fp;
	bool state;
	string ans;
	fp = fopen("A-large.in","r");
	FILE *fp1;
	fp1 = fopen("A-large.txt","w");
	if(fp1 == NULL)
	{
		printf("file could not be opened\n");
		getchar();
		return 0;
	}

	if(fp == NULL)
	{
		printf("File could not be opened\n");
		getchar();
		return 0;
	}
	else{
		fscanf(fp,"%d",&count);
		for(int index=0;index<count;index++)
		{
			fscanf(fp,"%d",&n);
			fscanf(fp,"%d",&k);
			snap snapObj(n,k);
			state = snapObj.stateSnap();
			/*if(state == false)
				ans = "OFF";
			else if(state == true)
				ans = "ON";*/

			fprintf(fp1,"Case #%d: %s",index+1,state?"ON":"OFF");
			fprintf(fp1,"\n");
		}
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}
			

		
