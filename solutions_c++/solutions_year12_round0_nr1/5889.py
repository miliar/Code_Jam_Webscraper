#include<iostream>
#include<string>

using namespace std;

int main(){
    char A[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    
    int charNum;
    char ch;
    int caseNum=0;
    cin>>caseNum;
    string line;
    int lineSize;

    getline(cin, line);
    for(int lineCount=1; lineCount<=caseNum; lineCount++){
 
        cout<<"Case #"<<lineCount<<": ";
        getline(cin, line);
        lineSize=line.size();
        for (int i=0; i<lineSize; i++) {
            if (line[i]!=' ') {
                charNum=line[i]-97;
                cout<<A[charNum];
            }
            else{
            cout<<" ";
            }
        }
        cout<<"\n";
    }
    return 0;
}