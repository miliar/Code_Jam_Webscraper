#include<iostream>
#include<vector>
#include<string>
#include<map>
using namespace std;

struct Path{
    std::string name;
    std::map<string,Path*> children;
};



int main(){
    int t;
    std::cin>>t;
    for(int tc=0;tc<t;tc++)
    {
        Path root;
        root.name="";
        int m,n;
        std::cin>>m>>n;
        for(int i=0;i<m;i++){
            std::string path;
            std::cin>>path;
            std::vector<string> parts;
            string cur;
            for(int j=1;j<path.size();j++){
                if(path[j]=='/'){
                    parts.push_back(cur);
                    cur="";
                }else{
                    cur.push_back(path[j]);
                }

            }
            parts.push_back(cur);

            Path* it = &root;
            for(int j=0;j<parts.size();j++){
                if(it->children.count(parts[j])){
                    it = it->children[parts[j]];
                }else {
                    it->children[parts[j]] = new Path();
                    //parts[j];
                    it = it->children[parts[j]];
                }
            }
        }
        int count = 0;
        for(int i=0;i<n;i++){
            std::string path;
            std::cin>>path;
            std::vector<string> parts;
            string cur;
            for(int j=1;j<path.size();j++){
                if(path[j]=='/'){
                    parts.push_back(cur);
                    cur="";
                }else{
                    cur.push_back(path[j]);
                }
            }
            parts.push_back(cur);

            Path* it = &root;
            for(int j=0;j<parts.size();j++){
                if(it->children.count(parts[j])){
                    it = it->children[parts[j]];
                    //std::cout<<"found "<<parts[j]<<std::endl;
                }else {
                    //std::cout<<"mkdir "<<parts[j]<<std::endl;
                    it->children[parts[j]] = new Path();
                    //parts[j];
                    count++;
                    it = it->children[parts[j]];
                }
            }
        }
        std::cout<<"Case #"<<tc+1<<": "<<count<<std::endl;
        
    }
}
