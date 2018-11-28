#include <iostream>
#define max_x 21
using namespace std;
int T, N, S[max_x];
int a[2000001][21];
int ok = 1;
#include<iostream>
#include<fstream>
#include<string>
#include<list>


using namespace std;

int subset(int arr[], int size, int left, int index, list<int> &l){
    ofstream fout1;
    fout1.open ("1.txt",ios::app);
    if(left==0){
        int sum = 0;
        int i = 1;
        for(list<int>::iterator it=l.begin(); it!=l.end() ; ++it){
            sum += *it;
        }
        if (a[sum][0] == 1){
            int j = 1;
            while (a[sum][j] > 0&&j<=20){
                fout1 << a[sum][j]<<" ";  
                j++;
            }
            fout1 << endl;
             
            for(list<int>::iterator it=l.begin(); it!=l.end() ; ++it){
                a[sum][i] = *it;
                fout1 << *it <<" ";
                i++;
            }   
            fout1 << endl;
           // system("pause");
            exit(1);
            return 1;
        }
        else{
            a[sum][0] = 1;
             for(list<int>::iterator it=l.begin(); it!=l.end() ; ++it){
                a[sum][i] = *it;
                i++;
             } 
            return 0;  
        }
    
    }
    for(int i=index; i<size;i++){
        l.push_back(arr[i]);
        subset(arr,size,left-1,i+1,l);
        l.pop_back();
    }
}     

int main(int argc, char* argv[]){
    ofstream fout;
    fout.open ("1.txt",ios::app);
    cin >> T;
    int x = (int)argv[1][0] - 48 + 1;
    cout << x << endl;
    for (int i=0; i<x;++i){
        //cout << "Case x"
        cin >> N;
        for (int j = 0; j<N;++j){
            cin >> S[j];    
        }    
    }
        fout <<"Case #"<<x <<":"<<endl;
        memset(a,0,sizeof(a));
        list<int> lt;
        for (int ii = 1; ii <= 20; ++ii){   
            subset(S,20,ii,0,lt);
        }
    
    //cout << "Imposible" <<endl;
    system("pause");
}

