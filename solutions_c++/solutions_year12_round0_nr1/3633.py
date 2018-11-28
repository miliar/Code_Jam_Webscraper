# include<iostream>
# include<fstream>
# include<strstream>
using namespace std;

int main(){
	ifstream fin("A-small-attempt7.in");
	char s1[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char buffer[101];
	fin.getline(buffer,101);
	int n=atoi(buffer);
	if(n>=1&&n<=30){
		ofstream myfile;
		myfile.open("output.txt");
		for(int g=0;g<n;g++){
			fin.clear();
			fin.getline(buffer,101);
			for(int i=0;buffer[i]!='\0';i++){
				if(buffer[i]!=' '){
					int ch=int(buffer[i])-97;
					buffer[i]=s1[ch];
				}
			}
			myfile<<"Case #"<<g+1<<": "<<buffer<<"\n";
		}
		myfile.close();
	}
	return(0);
}
