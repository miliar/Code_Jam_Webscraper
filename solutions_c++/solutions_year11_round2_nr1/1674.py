#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int testcases;
    cin>>testcases;
    for(int ii=0;ii<testcases;ii++){
        int n;
        cin>>n;
        vector<vector<char> > vov;
        for(int i=0;i<n;i++){
            vector<char> temp;
            for(int j=0;j<n;j++){
                char x;
                cin>>x;
                temp.push_back(x);
            }
            vov.push_back(temp);
        }
        vector<double> wp;
        for(int i=0;i<vov.size();i++){
            int count=0;int total=0;
            for(int j=0;j<vov[i].size();j++){
                if(vov[i][j]=='1'){
                    count++;
                    total++;
                }
                if(vov[i][j]=='0'){
                    total++;
                }
            }
            wp.push_back(count/(total*1.0));
        }
        
        vector<double> owp;
        for(int i=0;i<vov.size();i++){
            double avg=0;
            int avgcount=0;
            for(int j=0;j<vov.size();j++){
                if(j!=i && (vov[i][j]=='1' || vov[i][j]=='0')){
                    avgcount++;
                    int count=0;int total=0;
                    for(int k=0;k<vov.size();k++){
                        if(k!=i){
                            if(vov[j][k]=='1'){
                                count++;
                                total++;
                            }
                            if(vov[j][k]=='0'){
                                total++;
                            }
                        }
                    }
                   // cout<<i<<" "<<count/(total*1.0)<<endl;
                    avg+=count/(total*1.0);
                }
                
            }
            owp.push_back(avg/(avgcount));
        }
        vector<double> oowp;
        for(int i=0;i<owp.size();i++){
            double temp=0;
            int addcount=0;
            for(int j=0;j<owp.size();j++){
                if(i!=j && (vov[i][j]=='1' || vov[i][j]=='0')){
                    temp+=owp[j];
                    addcount++;
                }
            }
            oowp.push_back(temp/(addcount));
        }
        
        /*for(int i=0;i<oowp.size();i++){
            cout<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<endl;
        }*/
        cout<<"Case #"<<ii+1<<":"<<endl;
        for(int i=0;i<wp.size();i++){
            cout<<0.25*wp[i]+0.50*owp[i]+0.25*oowp[i]<<endl;
        }
    }
}