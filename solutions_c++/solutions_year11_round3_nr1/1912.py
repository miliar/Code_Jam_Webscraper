#include<vector>
#include<iostream>
#include<fstream>

#define FILE
using namespace std;

int main()
{
#if 1
	ifstream readStream;
	ofstream writeStream;

	readStream.open("A-large.in", ios::in);
	writeStream.open("A-large.out", ios::out);
#endif
	const int inputSize = 1000;
	char temp[inputSize];

	// First line
	readStream.getline(temp, inputSize, '\n');
	int nCase = atoi(temp);
	
	for(int i=0; i<nCase; i++)
	{
		readStream.getline(temp, inputSize, '\n');

		char *splitted;
		splitted = strtok(temp," ");
		int R = atoi(splitted);

		splitted = strtok(NULL," ");
		int C = atoi(splitted);

		char** tiles = new char*[R];
		for(int r=0; r<R; r++)
			tiles[r] = new char[C];

        for(int j=0;j<R;j++)
		{
			readStream.getline(temp, inputSize, '\n');
			cout<<temp<<endl;
            for(int k=0; k<C; k++)
			{
                tiles[j][k] = temp[k];
            }
        }

		bool possible=true;
        for(int j=0;j<R;j++){
            for(int k=0;k<C;k++){
                if(k!=C-1){
                    if(tiles[j][k]=='#'){
                        if(tiles[j][k+1]=='#'){
                            k++;
                        }else{
                            possible =false;
                            break;
                        }
                    }
                }else{
                    if(tiles[j][k]=='#'){
                        possible =false;break;
                    }
                }
            }
        }
        for(int k=0;k<C;k++){
            for(int j=0;j<R;j++){
                if(j!=R-1){
                    if(tiles[j][k]=='#'){
                        if(tiles[j+1][k]=='#') j++;
                        else{
                            possible =false;break;
                        }
                    }
                }else{
                    if(tiles[j][k]=='#'){
                        possible=false;break;
                    }
                }
            }
        }
        if(possible){
            int *countR = new int[R];
            int *countC = new int[C];
            for(int j=0;j<R;j++) countR[j]=0;
            for(int j=0;j<C;j++) countC[j]=0;
            for(int j=0;j<R;j++){
                for(int k=0;k<C;k++){
                    if(tiles[j][k]=='#'){
                        if((countR[j]%2==0)&&(countC[k]%2==0))tiles[j][k]='/';
                        else if((countR[j]%2==1)&&(countC[k]%2==0)) tiles[j][k]='\\';
                        else if((countR[j]%2==0)&&(countC[k]%2==1)) tiles[j][k]='\\';
                        else if((countR[j]%2==1)&&(countC[k]%2==1)) tiles[j][k]='/';
                        countR[j]++;countC[k]++;
                    }
                }
            }

            writeStream<<"Case #"<<i+1<<":"<<endl;
            for(int j=0;j<R;j++){
                for(int k=0;k<C;k++){
                    writeStream<<tiles[j][k];
                }
                writeStream<<endl;
            }
        }else{
            writeStream<<"Case #"<<i+1<<":"<<endl;
			writeStream<<"Impossible"<<endl;
        }
	}

	writeStream.clear();
	writeStream.close();

    return 0;
}
