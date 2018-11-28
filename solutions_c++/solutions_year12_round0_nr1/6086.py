#include<iostream>
#include<cstring>
#include<string>
using namespace std;

void CreateMappingTable(char table[200]) 
{
	char str[27] = "ynficwlbkuomxsevzpdrjgthaq";
	int i;
	int j = 0;
	for(i = 'a'; i <= 'z'; i++) {
	  table[str[j]] = i;
	  j++;
	}
}

int main(int argc,char** argv)
{
	char table[200];
	CreateMappingTable(table);
	char s[101];
	int n;
	cin>>n;
	int i = 1;
	string S;
	getline(cin,S);
	while(getline(cin,S)) {
		const char* str = S.c_str();
		strcpy(s,str);
		int j;
		for(j = 0; j < strlen(s); j++) {
		
			if (s[j] == ' ') continue;
			
			else
			  	s[j] = table[s[j]];
				  
		}

		cout<<"Case "<<"#"<<i<<": "<<s<<endl;
		i++;
	}
	return 0;
}



