#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream input;
	ofstream output;
	input.open("d:/input.in");
	output.open("d:/output.in");
	int N;
	input>>N;
	char *temp="yhesocvxduiglbkrztnwjpfmaq", *inp;
	inp=new char[110];
	input.getline(inp,110);
	for(int i=1;i<=N;i++){
		inp=new char[110];
		input.getline(inp,110);
		for(int j=0;j<110;j++)
			if(inp[j]>=97 && inp[j]<=122)
				inp[j]=temp[tolower(inp[j])-97];
		output<<"Case #"<<i<<": "<<inp<<"\n";
		cout<<"Case #"<<i<<": "<<inp<<"\n";
	}
	system("pause");
	return 0;
}