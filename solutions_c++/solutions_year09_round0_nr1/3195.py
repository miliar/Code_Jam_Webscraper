#include<fstream>
#include<iostream>
#include<string>
#include<math.h>

using namespace std;

int L,D,N;
bool chars[30][20];
string words[5010];
string ccase; //current case

bool isPossible(int dicNum)
{
	bool err=false;
	int p=0;
	char c;

	string s=words[dicNum];
	for (int i=0;i<L;i++){
		c=ccase[p++];
		if (c=='('){
			c=ccase[p++];
			err=true;
			do{
				if (c==s[i]) err=false;
				c=ccase[p++];
			} while (c!=')');
			if (err) return false;
		}
		else
			if (c!=s[i]) return false;
	}
	return true;
}

int main(){

	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int i,j,k;
	char c;
	
	fin>>L>>D>>N;
	memset(chars, false, 600);
	for (i=0;i<D;i++)
		fin>>words[i];

	for (i=0;i<D;i++){
		for (j=0;j<L;j++){
			c=words[i][j];
			chars[c-'a'][j]=true;
		}
	}

	//check cases
	for (int caseNum=0;caseNum<N;caseNum++)
	{
		fin>>ccase;
		int count=0;
		for (int i=0;i<D;i++)
			if (isPossible(i)) count++;
		fout<<"Case #"<<(caseNum+1)<<": "<<count<<endl;
		
	}

	system("pause");
	return 0;
}

