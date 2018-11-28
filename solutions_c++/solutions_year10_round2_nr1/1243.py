#include<iostream>
#include<vector>
#include<string>
#include<sstream>

#define sz(X) ((int)(X.size())) 
#define rep(i,s,n) for(int i=s; i<n; i++) 

using namespace std;

struct File
{
    string name;
    vector<File> ch;
};

File root;

int InsertFS(File &F, vector<string> &path, int ind)
{
    if(ind == sz(path)) return 0;
    rep(i,0,sz(F.ch))
      if(path[ind] == F.ch[i].name)
        return InsertFS(F.ch[i], path, ind+1);  

    File child;
    child.name = path[ind];
    F.ch.push_back(child);
    return InsertFS(F.ch[sz(F.ch) - 1], path, ind+1) + 1;
}


int main()
{
    int T;
    cin>>T;
    for(int k = 1; k <= T; k++)
    {
        int N,M;
        cin>>N>>M;
        string fileName;
        getline(cin, fileName);
        root.ch.clear();
        rep(i,0,N)
        {
            getline(cin, fileName, '\n');
            istringstream sin(fileName);
            char c;
            sin>>c;
            string dir;
            vector<string> path;
            while(true)
            {
                getline(sin, dir, '/');
                if(!sin) break;
                path.push_back(dir);
            }
            InsertFS(root, path, 0); 
        }

        int ans = 0;
        rep(i,0,M)
        {
            getline(cin, fileName, '\n');
            istringstream sin(fileName);
            char c;
            sin>>c;
            string dir;
            vector<string> path;
            while(true)
            {
                getline(sin, dir, '/');
                if(!sin) break;
                path.push_back(dir);
            }
            ans += InsertFS(root, path, 0); 
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }

    return 0;

}



