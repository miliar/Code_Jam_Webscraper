#include<iostream>
#include<string>
#include<vector>
#include<fstream>
using namespace std;

int sovle(vector<string> se, vector<string> qq)
{
    int r = 0;
    
    while(!qq.empty()) {
        
        int sen = 0; 
        int qqn = 0;
        int sn = 0;
        int qn = 0;;
        for(int i = 0; i < se.size(); i++) {
            bool f = true;
            for(int j = 0; j < qq.size(); j++) {
                if(se[i] == qq[j]) {
                    f = false;
                    sn = i;
                    qn = j;    
                    break;
                }
            }
            //cout << "tt: " << sn <<" "<< qn << endl;
            //cout << "f=" <<f<<endl;
            if(f) return r;
            
            
            if(qn > qqn) {
                qqn = qn;
                sen = sn;
            }
        }
        
        //cout << "tm: " << sen <<" "<< qqn << endl;
        
        //se.erase(se.begin()+sen);
        //for(int i = 0; i < se.size(); i++) cout << se[i] << " ";
        //cout << endl;
        qq.erase(qq.begin(),qq.begin()+qqn);
        //for(int i = 0; i < qq.size(); i++) cout << qq[i] << " ";
        //cout << endl;
        r++;
    }
    
    return r;
}
        
int main()
{
    ofstream out("F:\\t\\out1.txt");
    
    int n = 0;
    cin >> n;
    int idx = 1;
    
    while(n > 0) {
        int s = 0;
        cin >> s;
        cin.ignore();
        
        vector<string> se;
        for(int i = 0; i < s; i++) {
            string tmp = "";
            getline(cin,tmp);
            
            se.push_back(tmp);
        }
        //cout << endl;
        //for(int i = 0; i < s; i++) cout <<"lj "<< se[i] << endl;
        //cout << endl;
        
        int q = 0;
        cin >> q;
        cin.ignore();
        
        vector<string> qq;
        for(int i = 0; i < q; i++) {
            string tmp = "";
            getline(cin,tmp);
            
            qq.push_back(tmp);
        }
        
        //cout << endl;
        //for(int i = 0; i < q; i++) cout <<"lj "<< qq[i] << endl;
        //cout << endl;
        
        int r = sovle(se,qq);
        cout << "Case #" << idx << ": " << r << endl;
        out << "Case #" << idx << ": " << r << endl;
        idx++;
        n--;
    }
    
    out.close();
    system("pause");
    return 0;
}
    
