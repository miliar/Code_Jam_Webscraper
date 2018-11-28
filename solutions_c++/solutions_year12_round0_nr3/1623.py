// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <map>
#include <list>
#include <string>
#include <sstream>

using namespace std;



string shift(string in){
    if(in.length()<=1){
        return in;
    }
    string first=in.substr(0,1);
    string rest=in.substr(1);
    string out=rest.append(first);
    return out;
}

int main()
{

	int tests;
    int A, B;
    long count;
    map<int, list<int> > pairMap;
    for(int j=1;j<2000000;j++){
        list<int> myList;
        std::stringstream stream;
        stream << j;
        string st=stream.str();
        string sh=shift(st);
        while(sh.compare(st)!=0){
            if(sh[0]!='0'){
                int result;
                stringstream(sh) >> result;
                if(j<result){
                    myList.push_back(result);
                }
            }
            sh=shift(sh);
        }
        if(myList.size()>0){
           pairMap.insert(pair<int, list<int> >(j, myList));
        }
    }
    map<int,list<int> >::iterator mapit;
    list<int>::iterator listit;
	cin >> tests;
	for(int i = 1; i<=tests; i++){
        cin >> A;
        cin >> B;
        count=0;
        for(int j=A;j<B;j++){
            mapit=pairMap.find(j);
            if(mapit!=pairMap.end()){
                list<int> myList = mapit->second;
                for (listit=myList.begin(); listit != myList.end(); listit++ ){
                    if(*listit<=B){
                        count++;
                    }
                }
            }
        }
        cout << "Case #" << i << ": " << count << endl;
	}
}

