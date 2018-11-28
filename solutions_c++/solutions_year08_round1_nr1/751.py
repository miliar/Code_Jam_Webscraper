#include<fstream>
#include<vector>
#include<string>
#include<iostream>
#include<cstdio>
#include<set>
using namespace std;
int main()
{
    ifstream inFile;
    ofstream outFile;
    char inputFilename[] = "A-small-attempt0.in";
    char outputFilename[] = "out.list";
    inFile.open(inputFilename, ios::in);
    outFile.open(outputFilename, ios::out);
    int N=0;
    inFile >> N;
    //cout<<"N "<<N<<endl;
    for(int i=1;i<=N;++i)
    {
        int n=0;
        inFile >> n;
        //cout<<"n "<<n<<endl;
        vector<int> v1;
        for(int ii=0;ii<n;++ii)
        {
                int a=0;
                inFile >> a;
                v1.push_back(a);
        }
        vector<int> v2;
        for(int ii=0;ii<n;++ii)
        {
                int a=0;
                inFile >> a;
                v2.push_back(a);
        }        
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        reverse(v2.begin(),v2.end());
        //for(int ii=0;ii<n;++ii)
                //cout<<v1[ii]<<" "<<endl;
        long long res=0;
        for(int ii=0;ii<n;++ii)
                res+=(v1[ii]*v2[ii]);        
         outFile << "Case #"<<i<<": "<<res<<endl;
         //cout << "Case #"<<i<<": "<<res<<endl;
    }
    //cin>>N;
    inFile.close();
    outFile.close();
    return 0;
}
