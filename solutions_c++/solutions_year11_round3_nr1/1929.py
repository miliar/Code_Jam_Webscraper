//      A.cpp
//      
//      Copyright 2011 Kushagra Gour a.k.a. Chin Chang <chinchang457@gmail.com>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;

char arr[52][52];

bool check(int r, int c, int i, int j){
	if(i>=0 && i<r && j>=0 && j<c)
		if(arr[i][j]=='#') return true;
	return false;
}

int main(int argc, char** argv)
{
	FILE *f,*fo;
	f=fopen("A-large.in","r");
	fo=fopen("A_large_out.txt","w");
	int t,r,c;
	
	fscanf(f,"%d",&t);
	for(int test=1;test<=t;test++){
		bool poss=true;
		fscanf(f,"%d %d\n",&r,&c);
		
		
		int nob=0;
		// take input
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				fscanf(f,"%c",&arr[i][j]); //cout<<arr[i][j];
				
				if(arr[i][j]=='#'){
					nob++;
				}				
			}
			char c; fscanf(f,"%c",&c); //cout<<endl;
		}
		
		if(nob%4!=0) poss=false;
		else{
			for(int i=0;i<r && poss;i++){
				for(int j=0;j<c && poss;j++){
					
					if(arr[i][j]=='#'){
						check(r,c,i,j) ? arr[i][j]='/' : poss=false;
						check(r,c,i,j+1) ? arr[i][j+1]='\\' : poss=false;
						check(r,c,i+1,j+1) ? arr[i+1][j+1]='/' : poss=false;
						check(r,c,i+1,j) ? arr[i+1][j]='\\' : poss=false;
					}			
				}
			}
		}
		
		
		fprintf(fo,"Case #%d:\n",test);
		if(!poss) fprintf(fo,"Impossible\n");
		else{
			for(int i=0;i<r;i++){
				for(int j=0;j<c;j++){
					fprintf(fo,"%c",arr[i][j]);
				}
				fprintf(fo,"\n");
			}
		}
		
	}
	fclose(f); fclose(fo);
	return 0;
}
