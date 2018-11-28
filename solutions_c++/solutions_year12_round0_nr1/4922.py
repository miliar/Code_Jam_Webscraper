#include<iostream>
#include<fstream>
#include<string>
using namespace std;

char table[26];
void make_table(char* encoded,char* decoded){

	int n = strlen(encoded);
	for(int i=0;i<n;i++)
		if(isalpha(encoded[i]))
		table[encoded[i]-'a'] = decoded[i];
}
void decode(char* encoded,char* decoded){

	
	int n = strlen(encoded);
	int i;
	for(i=0;i<n;i++)
		if(isalpha(encoded[i]))
		decoded[i] = table[encoded[i]-'a'];
		else 
		decoded[i] = encoded[i];

	decoded[i]='\0';
	
}

int main(){
	
	char *idata[] = {"zqejp mysljylc kd kxveddknmc re jsicpdrysi",
					   "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
					   "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	char *odata[] = {"qzour language is impossible to understand",
					   "there are twenty six factorial possibilities",
					   "so it is okay if you want to just give up"};
	 
	for(int i=0;i<3;i++)
		make_table(idata[i],odata[i]);

	for(int i=0;i<26;i++)
		cout<<(char)('a'+i)<<":"<<table[i]<<"\n";

	char input[101];
	char decoded[101];
	int ncases;
	string input_path = "inputfile.txt";
	string output_path = "outputfile.txt";
	fstream in(input_path,ios::in);
	fstream out(output_path,ios::out);

	in>>ncases;
	//dummy
	in.getline(input,101);
	for(int i=0;i<ncases;i++){
		in.getline(input,101);

		decode(input,decoded);
		
		out<<"Case #"<<i+1<<": "<<decoded<<"\n";
	}

	in.close();
	out.close();


	return 0;

}