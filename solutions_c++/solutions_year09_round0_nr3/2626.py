# include <fstream>
# include <iostream>
# include <string>

using namespace std;

int main(int argc, char* argv[])
{
	int N;
	string first_line, input;
	string *words;
	int i_word, i_input, count;
	ifstream inFile;
	
	cerr << argv[1] << endl;
	cerr << argv[2] << endl;
    inFile.open(argv[1]);
	
	//outFile.open(argv[2]);
	if (!inFile.is_open()) 
	{
		cerr << "Unable to open input file " << argv[1] << endl;
		exit(1);   // call system to stop
    }

	FILE * outFile;
	outFile=fopen(argv[2],"w");

	// Initialize

	
	getline(inFile,first_line);
	cerr << first_line << endl;
	sscanf(first_line.data(), "%d\n", &N);
	cerr << "N=" << N << endl;
	words = new string[N];

	//Read Each string
	for (int i=0; i<N; i++)
	{
		getline(inFile, words[i]);
		//cerr << words[i] << endl;
	}
    
	
    string mystring="welcome to code jam";
     //cerr<<endl<<mystring<<endl;

	for (int i=0; i <N; i++)
	{


		int lBig= words[i].length();

		//cerr<<endl<<"entering words["<<i<<"]= "<<words[i];
		

		int lSmall=mystring.length();

		int **TableBS;
		//cerr<<endl;
		//cerr<<"lBig = "<<lBig<<endl;
		//cerr<<"lSmall ="<<lSmall<<endl;

		TableBS= new int*[lBig];

		for (int COL=0;COL<lBig;COL++)
			TableBS[COL]=new int[lSmall];

       //cerr<<endl<<"here"<<endl;

		for (int k=lBig-1;k>=0;k--)
			for(int m=lSmall-1;m>=0;m--)
			 TableBS[k][m]=0;
//cerr<<endl<<"here"<<endl;
		
			






		if(words[i].compare(lBig-1,1,mystring,lSmall-1,1)==0)
			TableBS[lBig-1][lSmall-1]=1;


		for (int k=lBig-2;k>=0;k--)
		{
		  if(words[i].compare(k,1,mystring,lSmall-1,1)==0)
			  TableBS[k][lSmall-1]=(TableBS[k+1][lSmall-1]+1)%10000;
		  else
				TableBS[k][lSmall-1]=TableBS[k+1][lSmall-1];
		}
//cerr<<endl<<"here2"<<endl;

	    for (int k=lBig-2;k>=0;k--)
		{

			for (int m=lSmall-2;m>=0;m--)
			{
				if (words[i].compare(k,1,mystring,m,1)!=0)
				{
					TableBS[k][m]=TableBS[k+1][m];
				}
				else
				{
					TableBS[k][m]=(TableBS[k+1][m]+TableBS[k+1][m+1])%10000;
				}
			}
		}

		fprintf(outFile,"Case #%d: %04d\n",i+1,TableBS[0][0]);

	}



	inFile.close();
	fclose(outFile);
}

