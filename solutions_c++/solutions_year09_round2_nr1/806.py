
#include<stdio.h>
#include<string.h>
#include<memory.h>
#include <stdlib.h>
#include <math.h>

class tree
{
	public:
	tree() { weight = 1.0; memset(f,0,20); left=NULL; right=NULL; }
	int build( char *bfr )
	{
		int ob = 0;
		while( bfr[ ob ] != '(' )
			ob++;
		int cb = strlen( bfr ) - 1;
		while( bfr[ cb ] != ')' )
			cb--;
		char stree[8500];
		memset(stree,0,85*100);
		strncpy(stree,bfr+ob+1,cb-ob-1);
		int curr = 0;
		while( stree[ curr ] < 33 )
			curr++;
		weight = atof( stree );
		while( stree[ curr ] > 32 )
			curr++;
		if( !stree[ curr ] )
			return 1;
		while( stree[ curr ] < 33 && stree[ curr ] != 0 )
			curr++;
		if( !stree[ curr ] )
			return 1;
		if( stree[ curr ] != '(' && stree[ curr ] != ')' )
		{
			int start = curr;
			while( stree[ curr ] > 47 )
				curr++;
			strncpy(f,stree+start,curr-start);
		}
		while( stree[ curr ] < 40 )
			curr++;
		if( stree[ curr ] == ')' )
			return 1;
		if( stree[ curr ] == '(' )
		{
			int level = 1;
			int start = curr;
			while( level )
			{
				curr++;
				if( stree[curr] == ')' )
					level--;
				else if( stree[curr] == '(' )
					level++;
			}
			char rtree[8500];
			memset(rtree,0,8500);
			strncpy(rtree,stree+start,curr-start+1);
			curr++;
			right = new tree;
			right->build( rtree );
			while( stree[ curr ] != '(' )
				curr++;
			memset(rtree,0,8500);
			strcpy(rtree,stree+curr);
			left = new tree;
			left->build( rtree );
		}
		return 1;
	}

	double weight;
	char f[ 20 ];
	tree *left;
	tree *right;
};


int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	if ( !fp )
		return 0;
	int N = 0;
	fscanf(fp, "%d\n", &N);
	for( int i = 1 ; i <= N ; i++ )
	{
		int L = 0;
		fscanf(fp, "%d\n", &L);
		char bfr[85*100];
		memset(bfr,0,85*100);
		for( int l = 0 ; l < L ; l++ )
		{
			char lbfr[100];
			fgets(lbfr,100,fp);
			strcat(bfr,lbfr);
		}
		tree T;
		T.build( bfr );
		int A = 0;
		fscanf(fp, "%d\n", &A);
		fprintf(ofp, "Case #%d:\n" , i );
		for( int a = 0 ; a < A ; a++ )
		{
			char lbfr[100];
			fgets(lbfr,100,fp);
			int curr = 0;
			while( lbfr[ curr ] == ' ' )
				curr++;
			while( lbfr[curr] != ' ' )
				curr++;
			curr++;
			int no = atoi( lbfr + curr );
			while( lbfr[curr] != ' ' )
				curr++;
			char fet[201][50];
			for( int i = 0 ; i < no ; i++ )
			{
				memset(fet[i],0,20);
				while( lbfr[ curr ] == ' ' )
					curr++;
				int start = curr;
				while( lbfr[curr] != ' ' )
					curr++;
				strncpy(fet[i],lbfr+start,curr-start);
				int tmp = strlen(fet[i])-1;
				while( fet[i][tmp]<33 )
					fet[i][tmp--]=0;
			}
			tree *ct = &T;
			double cute = 1.0;
			while( ct )
			{
				cute *= ct->weight;
				int ok = 0;
				if( ct->f[0] != 0 )
				{
					for( int f = 0 ; f < no && !ok ; f++ )
						if( !strcmp(ct->f,fet[f]) )
							ok = 1;
				}
				if( ok )
				{
					ct = ct->right;
				}
				else
					ct = ct->left;
			}
			fprintf(ofp, "%.7f\n" , cute );
		}
	}
	return 0;
}
