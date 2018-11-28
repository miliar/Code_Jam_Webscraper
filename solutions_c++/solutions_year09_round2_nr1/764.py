#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <stdio.h>
#include <set>
using namespace std;

struct Node {
        string feat;
        double p;
        struct Node* r;
        struct Node* f;
}; 
ifstream f;

void rtoken(struct Node* n)
{
    string s;
    f>>s;
    double p;
    f>>p;
    n->p =p;
    f>>s;
    if(s.compare(")")!=0){
        n->feat=s;
        n->r=new(struct Node);
        n->f=new(struct Node);
        rtoken(n->r);
        rtoken(n->f);
        f>>s;
    }
    else
    {

        n->r=NULL;
        n->f=NULL;
        n->feat=="";
    }
}

int main(int argc, char ** argv)
{
	int N;
	f.open(argv[1]);
	f >> N ;
		
	for(int n=0; n<N; ++n)
	{
        cout<<"Case #"<<n+1 <<":"<<endl;
        int L;
	    f>>L;
        int res;
        if(L==0) res=0;
        
        bool b;
        struct Node * root = new(struct Node);
        rtoken(root);

        int A;
        f>>A;

        for(int i=0;i<A;++i){
            string animal;
            f>>animal;
            int n;
            f>>n;
            vector<string> feats;
            for(int j=0;j<n;++j)
            {
                string feat;
                f>>feat;
                feats.push_back(feat);
            }
            double res=1.0;
            struct Node * node=root;
            while(true){
                res*=node->p;
                if(node->feat=="") break;
                bool b=false;
                for(int k=0;k<feats.size() && b==false;++k)
                {
                     if(node->feat.compare(feats[k])==0) {
                        b=true;
                     }
                }
                if(b==false){
                    node = node->f;
                }else{
                    node = node->r;
                }
            }
		    printf("%1.7f\n",res);
        }

	}


	return 0;
}
