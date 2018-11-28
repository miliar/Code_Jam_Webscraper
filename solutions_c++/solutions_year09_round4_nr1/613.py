#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    //ifstream cin;
    //cin.open("A1.in");
    //cin.open("A-small-attempt0.in");
    //cin.open("A-large.in");
    //ofstream cout;
    //cout.open(
    
    int n;
    cin>>n;
    string str;
    getline(cin, str);
    
    int ml[50];
    
    for (int i=0; i<n; ++i){
        int k;        
        cin >> k;
        getline(cin,str);
        for (int j=0; j<k; ++j){
            int max = -1;
            string str;
            getline(cin,str);
            //cout<<str<<endl;
            
            for (int l = 0; l<k; ++l){
                if (str[l]=='1')
                    max = l;
            }
            ml[j] = max;
            //cout<<ml[j]<<" ";
            
        }
        //cout<<endl;
        

        int ans = 0;
        for (int j = 0; j<k; ++j)
            if (ml[j]>j)
            {
                for (int l = j+1; l<k; ++l)
                    if (ml[l]<=j)
                    {
                        int t = ml[l];
                        for (int w = l; w>j; w--)
                            ml[w] = ml[w-1];
                        ml[j] = t;
                        ans += l-j;
                        break;
                    }
                // for (int l =0; l<k; ++l)
                //     cout<<ml[l]<<" ";
                // cout<<endl;
                
            }
        
        cout<<"Case #"<<i+1<<": "<< ans <<endl;
    }
    
    //cin.close();
    
}
