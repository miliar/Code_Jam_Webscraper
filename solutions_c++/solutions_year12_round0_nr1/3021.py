#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <fstream>
//#include <windows.h>

using namespace std;

string match="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	// FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	ifstream fg;
	fg.open( infile );
	ofstream ofp;
	ofp.open( outfile );
	
	int t;
	fg >> t;
	for(int i = 1;i <= t;i++)
	{
        char tmp[101];
        // fgets(tmp,101,fp);
        
        if( i == 1 ){
            fg.getline( tmp, 256 );
        }
        
        fg.getline( tmp, 256 );
        //printf("%d %s\n",i ,tmp);
        int len = strlen(tmp);
        for(int j = 0;j != len;j++)
        {
            if(tmp[j] == ' ')
            continue;
            tmp[j] = match[tmp[j]-'a'];
        }
        ofp << "Case #" << i << ": " << tmp << "\n";
    }
    //system("pause");
    return 0;
}
