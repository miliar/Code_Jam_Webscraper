#include <iostream>
#include <string>
#include <sstream>
#include <fstream>


using namespace std;

int main()
{


     ifstream infile;
     ofstream outfile;
	 infile.open ("A-large.in");
	 outfile.open ("output_file.in");
	 string T;
	 getline(infile,T);
	 stringstream buffer(T);
	 int X;
	  string L1;
	  string L2;
	  string L3;
	  string L4;
	  string temp;
	  char t='T';
	  char o='O';
	  char x='X';
	 buffer >> X;
	 int Flag_Draw=1;

    for (int i=1 ;i<=X ;i++)
    {
            Flag_Draw=1;
            getline(infile,L1);
            getline(infile,L2);
            getline(infile,L3);
            getline(infile,L4);
            if(((L1[0]==t||L1[0]==o)&&(L1[1]==t||L1[1]==o)&&(L1[2]==t||L1[2]==o)&&(L1[3]==t||L1[3]==o))||((L2[0]==t||L2[0]==o)&&(L2[1]==t||L2[1]==o)&&(L2[2]==t||L2[2]==o)&&(L2[3]==t||L2[3]==o))||((L3[0]==t||L3[0]==o)&&(L3[1]==t||L3[1]==o)&&(L3[2]==t||L3[2]==o)&&(L3[3]==t||L3[3]==o))||((L4[0]==t||L4[0]==o)&&(L4[1]==t||L4[1]==o)&&(L4[2]==t||L4[2]==o)&&(L4[3]==t||L4[3]==o))||((L1[0]==t||L1[0]==o)&&(L2[0]==t||L2[0]==o)&&(L3[0]==t||L3[0]==o)&&(L4[0]==t||L4[0]==o))||((L1[1]==t||L1[1]==o)&&(L2[1]==t||L2[1]==o)&&(L3[1]==t||L3[1]==o)&&(L4[1]==t||L4[1]==o))||((L1[2]==t||L1[2]==o)&&(L2[2]==t||L2[2]==o)&&(L3[2]==t||L3[2]==o)&&(L4[2]==t||L4[2]==o))||((L1[3]==t||L1[3]==o)&&(L2[3]==t||L2[3]==o)&&(L3[3]==t||L3[3]==o)&&(L4[3]==t||L4[3]==o))||((L1[0]==t||L1[0]==o)&&(L2[1]==t||L2[1]==o)&&(L3[2]==t||L3[2]==o)&&(L4[3]==t||L4[3]==o))||((L1[3]==t||L1[3]==o)&&(L2[2]==t||L2[2]==o)&&(L3[1]==t||L3[1]==o)&&(L4[0]==t||L4[0]==o)))
            {outfile<<"Case #"<<i<<": O won"<<endl;
            cout<<i<<endl;
            }
            else if(((L1[0]==t||L1[0]==x)&&(L1[1]==t||L1[1]==x)&&(L1[2]==t||L1[2]==x)&&(L1[3]==t||L1[3]==x))||((L2[0]==t||L2[0]==x)&&(L2[1]==t||L2[1]==x)&&(L2[2]==t||L2[2]==x)&&(L2[3]==t||L2[3]==x))||((L3[0]==t||L3[0]==x)&&(L3[1]==t||L3[1]==x)&&(L3[2]==t||L3[2]==x)&&(L3[3]==t||L3[3]==x))||((L4[0]==t||L4[0]==x)&&(L4[1]==t||L4[1]==x)&&(L4[2]==t||L4[2]==x)&&(L4[3]==t||L4[3]==x))||((L1[0]==t||L1[0]==x)&&(L2[0]==t||L2[0]==x)&&(L3[0]==t||L3[0]==x)&&(L4[0]==t||L4[0]==x))||((L1[1]==t||L1[1]==x)&&(L2[1]==t||L2[1]==x)&&(L3[1]==t||L3[1]==x)&&(L4[1]==t||L4[1]==x))||((L1[2]==t||L1[2]==x)&&(L2[2]==t||L2[2]==x)&&(L3[2]==t||L3[2]==x)&&(L4[2]==t||L4[2]==x))||((L1[3]==t||L1[3]==x)&&(L2[3]==t||L2[3]==x)&&(L3[3]==t||L3[3]==x)&&(L4[3]==t||L4[3]==x))||((L1[0]==t||L1[0]==x)&&(L2[1]==t||L2[1]==x)&&(L3[2]==t||L3[2]==x)&&(L4[3]==t||L4[3]==x))||((L1[3]==t||L1[3]==x)&&(L2[2]==t||L2[2]==x)&&(L3[1]==t||L3[1]==x)&&(L4[0]==t||L4[0]==x)))
                {


                outfile<<"Case #"<<i<<": X won"<<endl;
                cout<<i<<endl;
                }

            else {
                for(int j=0 ;j<4;j++){
                    if(L1[j]=='.'||L2[j]=='.'||L3[j]=='.'||L4[j]=='.')
                    {
                        Flag_Draw=0;
                        break;
                    }
                }

                if(Flag_Draw==1)
                {
                    outfile<<"Case #"<<i<<": Draw"<<endl;
                    cout<<i<<endl;
                }

                else{
                    cout<<i<<endl;

                     outfile<<"Case #"<<i<<": Game has not completed"<<endl;
                }
            }

        getline(infile,temp);
    }
    return 0;

}
