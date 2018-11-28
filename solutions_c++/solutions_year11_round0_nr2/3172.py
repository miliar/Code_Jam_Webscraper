#include<iostream>
#include<string>
#include<cstring>
#include<fstream>
#include<vector>
#include<sstream>
using namespace std;
int main(){
    int i,j,k,l,m,n,comsize,clearsize,length,bufftop;
    //stringstream ss;
    string s;
    bool done;
    char input[40],buffer[40];
    ifstream readfile("TS.txt");
    readfile>>n;
    string results[n];
    string combinations[40];
    string temp;
    string clearence[40];
    vector<string> outset;
    for(i=0;i<n;i++){
        readfile>>comsize;
        for(j=0;j<comsize;j++){
            readfile>>temp;
            combinations[j]=temp;
        }
        readfile>>clearsize;
        for(j=0;j<clearsize;j++){
            readfile>>temp;
            clearence[j]=temp;
        }
        readfile>>length;
        readfile>>input;
        buffer[0]=input[0];
        bufftop=0;
        for(j=1;j<length;j++){
            done=false;
            if(bufftop==-1){
                bufftop=0;
                buffer[bufftop]=input[j];
                continue;
            }
            for(k=0;k<comsize;k++){
                if((buffer[bufftop]==combinations[k].at(0))&&(input[j]==combinations[k].at(1))){
                    buffer[bufftop]=combinations[k].at(2);
                    done=true;
                    break;
                }
                else if((buffer[bufftop]==combinations[k].at(1))&&(input[j]==combinations[k].at(0))){
                    buffer[bufftop]=combinations[k].at(2);
                    done=true;
                    break;
                }
            }
            if(!done){
                for(k=0;k<=bufftop;k++){
                    for(l=0;l<clearsize;l++){
                        if((buffer[k]==clearence[l].at(0))&&(input[j]==clearence[l].at(1))){
                            done=true;
                            bufftop=-1;
                        }
                        else if((buffer[k]==clearence[l].at(1))&&(input[j]==clearence[l].at(0))){
                            done=true;
                            bufftop=-1;
                        }
                    }
                    if(done)
                        break;
                }
            }
            if(!done){
                bufftop++;
                buffer[bufftop]=input[j];
            }
        }
        if(bufftop==-1){
            outset.push_back("[]");
        }
        else{
            outset.push_back("[");
            for(j=0;j<=bufftop;j++){
                stringstream ss;
                ss<<buffer[j];
                ss>>s;
                outset.at(i).append(s);
                if(j!=bufftop){
                    outset.at(i).append(", ");
                }
                else {
                    outset.at(i).append("]");
                }
            }
        }
    }
    ofstream outfile;
    outfile.open("OH.txt");
    for(i=0;i<n;i++){
        outfile<<"Case #"<<i+1<<": "<<outset.at(i)<<endl;
    }
    return 0;
}
