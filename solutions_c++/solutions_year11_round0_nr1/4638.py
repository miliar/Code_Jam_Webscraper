#include<iostream>
#include<vector>
#include<cmath>
#include<cstdio>
#include<fstream>
using namespace std;

int main(int argc,char *argv){
    int T,N,n,c2;
    vector<int> v1,v2;
    string s;
    char c1,sc2[4];


	ofstream f("D:/result.txt");
	ifstream ifile("D:/input.in");
	ifile>>T;
    for(int i=1;i<=T;i++){
        v1.clear();
        v2.clear();
        s.clear();

        ifile>>N;
        n=N;

        while(n--){
            ifile>>c1;
            ifile>>c2;
            s+=c1;
			sprintf(sc2,"%d",c2);
            s+=sc2;
            if(c1=='O')
                v1.push_back(c2);
            else if(c1=='B')
               v2.push_back(c2);
        }

        int pos1=1,pos2=1;
		vector<int>::iterator it1=v1.begin(),it2=v2.begin();
		int result=0;
		for(string::iterator  it = s.begin(); it!=s.end();){
				if(*it=='O'){
					int steps = abs(*it1-pos1)+1;
					result+=steps;
					pos1=*it1;
					++it1;
					if(it2!=v2.end()){
						if(steps>=abs(*it2-pos2))
							pos2=*it2;
						else{
								if(pos2<*it2)
									pos2+=steps;
								if(pos2>*it2)
									pos2-=steps;
						}
					}
				}
				else if(*it=='B'){
					int steps = abs(*it2-pos2)+1;
					result+=steps;
					pos2=*it2;
					++it2;
					if(it1!=v1.end()){
						if(steps>=abs(*it1-pos1))
							pos1=*it1;
						else{
								if(pos1<*it1)
									pos1+=steps;
								if(pos1>*it1)
									pos1-=steps;
						}
					}
				}
				++it;
				while(it!=s.end()){
					if(*it=='B'||*it=='O') break;
					++it;
				}
		}
		cout<<"Case #"<<i<<": "<<result<<endl;
		f<<"Case #"<<i<<": "<<result<<endl;
    }
	f.close();
	ifile.close();
}
