#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define li		long long
#define rep(i,to)	for(li i=0;i<((li)to);i++)
#define pb		push_back
#define sz(v)		((li)v.size())


int main(){
	ifstream ifs;
	ofstream ofs;
	ifs.open("input.txt");
	ofs.open("output.txt");
	FILE *fp;
	FILE *f;
	f=fopen("input.txt","r");
	fp=fopen("output.txt","w");
	
	li t;
	fscanf(f,"%lld",&t);
	rep(stage,t){
		li r,c,d;
		fscanf(f,"%lld%lld%lld",&r,&c,&d);
		li sum[505][505];
		li mp[505][505];
		li yw[505][505];
		li xw[505][505];
		rep(i,r){
			char str[505];
			fscanf(f,"%s",str);
			rep(j,c) mp[i][j]=(str[j]-'0')+d;
		}
		rep(i,r)rep(j,c){
			if(i!=0){
				if(j!=0) sum[i][j]=sum[i-1][j]+sum[i][j-1]+mp[i][j]-sum[i-1][j-1];
				else sum[i][j]=sum[i-1][j]+mp[i][j];
			}else{
				if(j!=0) sum[i][j]=sum[i][j-1]+mp[i][j];
				else sum[i][j]=mp[i][j];
			}
		}
		rep(i,r)rep(j,c){
			if(i!=0){
				if(j!=0) yw[i][j]=yw[i-1][j]+yw[i][j-1]+(j*2+1)*mp[i][j]-yw[i-1][j-1];
				else yw[i][j]=yw[i-1][j]+(j*2+1)*mp[i][j];
			}else{
				if(j!=0) yw[i][j]=yw[i][j-1]+(j*2+1)*mp[i][j];
				else yw[i][j]=(j*2+1)*mp[i][j];
			}
//			cout<<yw[i][j]<<endl;
		}
//		cout<<" "<<endl;
		rep(i,r)rep(j,c){
			if(i!=0){
				if(j!=0) xw[i][j]=xw[i-1][j]+xw[i][j-1]+(i*2+1)*mp[i][j]-xw[i-1][j-1];
				else xw[i][j]=xw[i-1][j]+(i*2+1)*mp[i][j];
			}else{
				if(j!=0) xw[i][j]=xw[i][j-1]+(i*2+1)*mp[i][j];
				else xw[i][j]=(i*2+1)*mp[i][j];
			}
//			cout<<xw[i][j]<<endl;
		}
			
		li res=0;
		rep(i,r)rep(j,c)for(li k=3;k+i-1<r && k+j-1<c;k++){
			li s=sum[i+k-1][j+k-1];
			if(i!=0) s-=sum[i-1][j+k-1];
			if(j!=0) s-=sum[i+k-1][j-1];
			if(i!=0 && j!=0) s+=sum[i-1][j-1];
			s-=mp[i][j];
			s-=mp[i+k-1][j];
			s-=mp[i][j+k-1];
			s-=mp[i+k-1][j+k-1];
			li y=yw[i+k-1][j+k-1];
			if(i!=0) y-=yw[i-1][j+k-1];
			if(j!=0) y-=yw[i+k-1][j-1];
			if(i!=0 && j!=0) y+=yw[i-1][j-1];
			y-=mp[i][j]*(2*j+1);
			y-=mp[i+k-1][j]*(2*j+1);
			y-=mp[i][j+k-1]*(2*(j+k-1)+1);
			y-=mp[i+k-1][j+k-1]*(2*(j+k-1)+1);
			li x=xw[i+k-1][j+k-1];
			if(i!=0) x-=xw[i-1][j+k-1];
			if(j!=0) x-=xw[i+k-1][j-1];
			if(i!=0 && j!=0) x+=xw[i-1][j-1];
			x-=mp[i][j]*(2*i+1);
			x-=mp[i+k-1][j]*(2*(i+k-1)+1);
			x-=mp[i][j+k-1]*(2*i+1);
			x-=mp[i+k-1][j+k-1]*(2*(i+k-1)+1);
			if(s*(i*2+k)==x && s*(j*2+k)==y) res=max(res,k);
//			cout<<i<<","<<j<<":"<<k<<" : "<<s*(i*2+k)<<" "<<s*(j*2+k)<<" "<<x<<" "<<y<<endl;
		}
		if(res==0) fprintf(fp,"Case #%lld: IMPOSSIBLE\n",stage+1);
		else fprintf(fp,"Case #%lld: %lld\n",stage+1,res);
	}	
			

	ifs.close();
	ofs.close();
}
