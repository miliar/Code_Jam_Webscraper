// speed1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
using namespace std;


typedef long long bigint;
const int max_n=500000;
const int max_m=500000;
const int modulus=1000000007;

int n;
struct sign_t
{	
	bigint speed;
	bigint variants;
} ;
sign_t signs[max_n];


void calc_variants_for_sign(int idx)
{
	bigint variants=1;//me only	
	bigint speed=signs[idx].speed;
	for (int i=idx+1;i<n;++i)
		if (signs[i].speed>speed)
			//variants+=signs[i].variants;
			variants+=(signs[i].variants%modulus);
	signs[idx].variants=variants;
}
void calc_all_signs()
{
	for (int i=n-1;i>=0;--i)
		calc_variants_for_sign(i);
}
bigint get_result()
{
	calc_all_signs();
	bigint result=0;
	for (int i=0;i<n;++i)
		result+=(signs[i].variants%modulus);		
	return result%modulus;
}

/*************************************
*generator, input
*************************************/
bigint genA[max_m];
bigint m,X,Y,Z;

void generate_speeds()
{
	for (bigint i=0;i<n;++i)
	{		
		signs[i].speed=genA[i%m];
		//signs[i].variants=0;
		genA[i%m]=(X*genA[i%m]+Y*(i+1))%Z;
	}

	//dbg: for (bigint i=0;i<n;++i) cout<<signs[i].speed<<"\n";
}

int _tmain(int argc, _TCHAR* argv[])
{	
	// !!!
	//DONT FORGET ABOUT MOD, PETROVICH! 
	// !!!
	
	
	ifstream fin("E:\\_fun\\r1C\\speed\\_input");
	ofstream fout("E:\\_fun\\r1C\\speed\\_out");
	int N;
	fin>>N;
	assert(fin.good());	if (!fin.good()) cerr<<"!!! fin not good!!!\n";//for release mode
	
	for (int i=1;i<=N;++i)
	{
		cout<<i<<"\n";
		fin>>n>>m>>X>>Y>>Z;
		for (int z=0;z<m;++z)
			fin>>genA[z];

		generate_speeds();
		fout<<"Case #"<<i<<": "<<get_result()<<"\n";
		
	}
	fout.flush();
	
	assert(fin.good() || fin.eof());if (!(fin.good()||fin.eof())) cerr<<"!!! fin not good at the end!!!\n";//for release mode
	
	cout<<"\7Done";
	int k;cin>>k;

	return 0;
}

/*dbg
	//case 2
	//n=6; m=2; X=2; Y=1000000000; Z=6;	
	//genA[0]=1; 	genA[1]=2;
	//case 1
	//n=5;m=5;X=0;Y=0;Z=5;
	//genA[0]=1; 	genA[1]=2;genA[2]=1; genA[3]=2;genA[4]=3;
	generate_speeds();
	cout<<get_result()<<"\n";
end dbg*/