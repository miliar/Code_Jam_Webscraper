#include<iostream>
#include<fstream>
#include<iomanip> 
using namespace std;

char match[20] = {'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m','\0'}; 
int acc[2][1000];
int counter = 0; 
int main()
{
	ofstream fout("out");
	char word[1000];
	int test;
	cin >> test;
	cin.getline(word,10);
	int num = 1;
	while( test > 0)
	{
		test--;
		cin.getline(word,1000);
		{ 
			if(word[0]=='\0')
				continue;
			for(int i =0;i<1000;i++)
				acc[0][i] = acc[1][i] = 0; 
			counter = 0;
			int length = strlen(word); 
			acc[0][length-1] = 0;
			acc[1][length-1] = 0; 
			for(int j=length-1;j>=16& j<=length;j--)
				if( word[j] == 'm')
				{
					counter++;
					acc[0][j-1] = counter; 
				}
				else
					acc[0][j-1] = acc[0][j]; 
			int now,old;
			
			now = 0;
			old = 1; 
			for(int i = 17;i>=1;i--) 
			{	//	for(int k=0;k<length;k++)
				//cout << acc[now][k] << ' ';
			//	cout << endl;
				//system("pause"); 
				old ^= now ^= old ^= now; 
				counter = 0; 
				for(int j=length-1;j>=i;j--)
					if( word[j]==match[i] )
					{ 
						acc[now][j-1] = acc[old][j]+counter; 
						acc[now][j-1] %=10000;
						counter += acc[old][j];
						counter %= 10000; 
					}
					else
						acc[now][j-1] = acc[now][j];
		
			}
			counter = 0; 
			for(int j=length-1;j>=0;j--)
				if( word[j] == 'w' )
				{
					counter+= acc[now][j];
					counter %= 10000; 
				} 
			fout << "Case #" << num++ << ": ";
			fout << setw(4) << setfill('0') << counter << endl; 
		} 
	}
} 
