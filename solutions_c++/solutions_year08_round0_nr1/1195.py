#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool compare(char* c1, char* c2);

int main(int argc, char* argv[])
{
    if( argc < 2 )
    {
	std::cout << "Please enter input file!" << std::endl;
	exit(1);
    }

    FILE* fp = fopen(argv[1], "r");
    if( fp == NULL )
    {
	std::cout << "Input file open failed!" << std::endl;
	exit(1);
    }

    FILE* fpout = fopen("output", "w");
    if( fpout == NULL )
    {
	std::cout << "Output file create failed!" << std::endl;
	exit(1);
    }
    
    int caseNum;
    char caseNum_s[10];
    fgets(caseNum_s, 10, fp);
    caseNum = atoi(caseNum_s);
    
    int engineNum, queryNum;
    char** engine;
    char** query;
    bool* used;
    //vector<char*> engine;
    //vector<char*> query;

    for( int i = 0; i < caseNum; i++ )
    {
	 char engineNum_s[10];
	 fgets(engineNum_s, 10, fp);
	 engineNum = atoi(engineNum_s);
	 //cout << engineNum << endl;
	 engine = new char*[engineNum];
	 used = new bool[engineNum];
	 //vector<char*> engine(engineNum);
	 for( int j = 0; j < engineNum; j++ )
	 {
	     engine[j] = new char[100];
	     fgets(engine[j], 100, fp);
	     used[j] = false;
	 }

	 //for( int j = 0; j < engineNum; j++ )
	   //  std::cout << engine[j];
	 
	 char queryNum_s[10];
	 fgets(queryNum_s, 10, fp);
	 queryNum = atoi(queryNum_s);
	 //cout << queryNum << endl;
	 query = new char*[queryNum];
	 //vector<char*> query(queryNum);
	 for( int j = 0; j < queryNum; j++ )
	 {
	     query[j] = new char[100];
	     fgets(query[j], 100, fp);
	 }

	 //for( int j = 0; j < queryNum; j++ )
	   //  std::cout << query[j];

	 int count = 0;
	 int switchNum = 0;
	 for( int j = 0; j < queryNum; j++ )
	 {
	     /*if( count == 4 )
	     {
		 switchNum++;
		 count = 0;
	     }*/
	     int p;

	     for( int k = 0; k < engineNum; k++ )
	     {
		 if( compare( query[j], engine[k]) )
		 {
		     if( used[k] == false )
		     {
			 used[k] = true;
			 p = k;
			 count++;
		     }
		     break;
		 }
	     }

	     if( count == engineNum )
	     {
		 switchNum++;
		 count = 1;
		 for( int x = 0; x < engineNum; x++ )
		     used[x] = false;
		 used[p] = true;
	     }
	     //cout << "count " << count << endl;
	     //cout << used[0] << " " << used[1] << " " << used[2] << " " << used[3] << " " << used[4] << endl;
	 }
	 
	 //cout << switchNum << endl;
	 fprintf(fpout, "Case #%d: %d\n", i+1, switchNum); 
	     
    }

    fclose(fp);
    fclose(fpout);
    
    return 0;
}

bool compare( char* c1, char* c2 )
{
    char cc1 = *c1, cc2 = *c2;
    int index = 0;
    while( cc1 != '\0' && cc2 != '\0'  )
    {
	if( cc1 != cc2 )
	    break;

	index++;
	cc1 = *(c1+index);
	cc2 = *(c2+index);
    }

    if( cc1 == cc2 )
	return true;
    else 
	return false;
}
    
