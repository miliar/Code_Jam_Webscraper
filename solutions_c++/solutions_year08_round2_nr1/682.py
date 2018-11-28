#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stdio.h>

#define MAX_TIME_LENGTH 10

using namespace std;

void handleCase(int caseNo,FILE* fp)
{
    int n,A,B,C,D,x0,y0,M;
    fscanf (fp,"%d %d %d %d %d %d %d %d",&n,&A,&B,&C,&D,&x0,&y0,&M);
    //printf ("Read: %d %d %d %d %d %d %d %d",n,A,B,C,D,x0,y0,M);

    long long X=x0,Y=y0,treeX[n],treeY[n];
    treeX[0] = x0; treeY[0] = y0;
    
    for (int i = 1;i <= n-1;i++)
    {   //  Generating tree coordinates.
	X = (A * X + B) % M;
	treeX[i] = X;
  	Y = (C * Y + D) % M;
	treeY[i] = Y;
	//cout << "(" << X << "," << Y << ")" << endl;
    }

    int nTriangles=0;
    for (int i=0;i<n;i++)
	for (int j=i+1;j<n;j++)
	    for (int k=j+1;k<n;k++)
		if (  (((treeX[i] + treeX[j] + treeX[k]) % 3) == 0) && (((treeY[i] + treeY[j] + treeY[k]) % 3) == 0)  )
		    nTriangles++;

    cout << "Case #" << (caseNo + 1) << ": " << nTriangles << endl;

    return;



}

int main(int argc, char* argv[])
{
	int nTestCases=0;
	FILE* fp = fopen (argv[1],"r");
	fscanf (fp,"%d",&nTestCases);
	//cout << nTestCases << " cases in all.";
	for (int i=0;i<nTestCases;i++)
		handleCase(i,fp);

	fclose(fp);
	return 0;
	
}

