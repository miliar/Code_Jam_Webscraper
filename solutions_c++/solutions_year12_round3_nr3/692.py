#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<fstream>
#include<cmath>
#include<set>
#include<map>
#include<string>
#include<utility>
#include<string.h>
#include<stdio.h>
#include<stack>
#include<queue>
#include<fstream>
using namespace std;
//bool Arr[1010][1010];
//bool verticies[1010];
//int n;
//int dfs (int index,int searchFor){
//	int count=0;
//	if (index==searchFor)
//		return 1;
//	verticies[index]=false;
//	for (int i=0;i<n;++i){
//		if (!Arr[index][i]||!verticies[i])
//			continue;
//		count+74=(dfs(i,searchFor));
//	}
//	verticies[index]=true;
//	return count;
//}
long long ArrA[101],Arra[101],Arrb[101],ArrB[101];
long long dfs (int indexa,int indexb,long long qnta,long long qntb,int n,int m){
	long long count=0;
	if (indexa>n-1||indexb>m-1)
		return 0;
	while (ArrA[indexa]==ArrB[indexb]){
		if (Arra[indexa]-qnta>Arrb[indexb]-qntb){

			qnta+=Arrb[indexb]-qntb;
			long long temp=Arrb[indexb]-qntb;
			count+=temp;
			indexb++;
			qntb=0;
		}
		else if (Arra[indexa]-qnta<Arrb[indexb]-qntb){
			qntb+=Arra[indexa]-qnta;
			count+=Arra[indexa]-qnta;
			qnta=0;
			indexa++;
		}
		else{
			count+=Arra[indexa]-qnta;
			qnta=0;
			qntb=0;
			indexa++;indexb++;
		}
	}
	long long temp=dfs(indexa,indexb+1,qnta,0,n,m);
	long long temp1=dfs(indexa+1,indexb,0,qntb,n,m);
	count+=(temp>temp1)?temp:temp1;
	return count;
}
int main (){
	ifstream in ("C-small-attempt3 (2).in");
	ofstream out ("A.out");
	int T;
	in>>T;
//	T=1;
//	for (int i=0;i<T;++i){
//
//		memset(Arr,false,sizeof(Arr));
//		memset (verticies,true,sizeof(verticies));
//		int m;
//		in>>n;
//		for (int j=0;j<n;++j){
//			in>>m;
//			for (int k=0;k<m;++k){
//				int reader;
//				in>>reader;
//				Arr[j][reader-1]=true;
//			}
//		}
//		bool yes=false;
//		for (int j=0;j<n&&!yes;++j){
//			for (int k=j+1;k<n&&!yes;++k){
//
//				if (dfs (j,k)>=2){
//					yes=true;
//				}
//			}
//		}
//		out<<"Case #"<<i+1<<": ";
//		if (yes)
//			out<<"Yes"<<endl;
//		else
//			out<<"No"<<endl;
//	}
	for (int i=0;i<T;++i){
		int n,m;
		in>>n>>m;
		memset(ArrA,0,sizeof(ArrA));
		memset(ArrB,0,sizeof(ArrB));
		memset(Arra,0,sizeof(Arra));
		memset(Arrb,0,sizeof(Arrb));
		for (int j=0;j<n;++j){
			long long a,A;
			in>>a>>A;
			ArrA[j]=A;
			Arra[j]=a;
		}
		for (int j=0;j<m;++j){
			long long b,B;
			in>>b>>B;
			ArrB[j]=B;
			Arrb[j]=b;
		}
		out<<"Case #"<<i+1<<": "<<dfs(0,0,0,0,n,m)<<endl;
	}
	return 0;
}
