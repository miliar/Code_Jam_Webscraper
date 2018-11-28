#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <iomanip>


using namespace std;

//max word length
#define W_L 16
//size of lowercase letters  //if it will be more letter the unsigned long is not good as set
#define W_S 26
//binary set represent of item of id X
#define ID2BIT(X) ( 1<<(X-1) )
//convert letter to ID
#define L2ID(X) ( (X)&(~96) )

#define ALL_LETTERS ((1<<W_S)-1)
//return
///if returns 0 means no element in set
int GetElement(unsigned long set) {
    int begin=0;
    int end=W_S;
    int x=end;
    unsigned long xx;
    if (set==0) return 0;
    if (!(set&ALL_LETTERS)) return 0;
    while (!(ID2BIT(x)&set)) {
        x=(begin+end)/2;
        xx=ID2BIT(x);
        if (set<=xx) end=x;
        else begin=x;
    }
    return x;
}

inline void zeroWord(char* word) {
    for (int x=0;x<=W_L;x++)word[x]=0;
}
//word length
int WL=0;
//number of test
int N_TESTS=0;


class TreeElement {
public:
    TreeElement() {
        for (int x=0;x<=W_L;x++)filter[x]=0;
        parent=0;
    }
    char letter;
    unsigned long filter[W_L];//maybe change for WL
    TreeElement* childs[W_S+1];
    TreeElement* parent;
    void add(char* word,int level) {
        //check for exist leter in child
        TreeElement* child;
        if (!(filter[level]&ID2BIT(word[level]))) {
            //create new child
            child=new TreeElement();
            child->parent=this;
            child->letter=word[level];
            filter[level]|=ID2BIT(word[level]);
            childs[word[level]]=child;
            //propagate up
            TreeElement* parent=this;
            for (int x=level-1;x>=0;x--) {
                parent=parent->parent;
                if ( (parent->filter[level] )&ID2BIT(word[level])) break;
                parent->filter[level]|=ID2BIT(word[level]);
            }
        }
        if (level+1==WL) return;
        //cout<<int(word[level])<<endl;
        //cout<<childs[word[level]]<<endl;
        //cout<<"---"<<endl;
        childs[word[level]]->add(word,level+1);
    }
    unsigned long check(unsigned long *query,int level) {
        unsigned long s=0;
        for (int x=WL-1;x>=level;x--) {
            s=filter[x];
			s&=query[x];
			if(!s) break;
        };
        return s;
    }

    void printtree(int level) {
        for (int x=0;x<level;x++) cout<<"-";
        cout<<int(letter)<<endl;
        unsigned long s=filter[level];
        while (s) {
            int z=GetElement(s);
            s&=~ID2BIT(z);
            childs[z]->printtree(level+1);
        };
    }
};

int find(vector<TreeElement*>& tree, unsigned long *query,int level) {
	vector<TreeElement*> next;
	unsigned long s;
	for (vector<TreeElement* >::const_iterator it=tree.begin();it!=tree.end();it++){
	   s=((*it)->check(query,level));
	   while (s) {
            int z=GetElement(s);
            s&=~ID2BIT(z);
			next.push_back( (*it)->childs[z]);
        };
	}
	
	if (level+1==WL) return next.size();
    return find(next,query,level+1);
}

void query(unsigned long *set,string s) {
    int pos=0;
    const char* ss=s.c_str();
    for (int x=0;x<WL;x++) {
        set[x]=0;
        if (ss[pos]=='(') {
            pos++;
            while (ss[pos]!=')') {
                set[x]|=ID2BIT( L2ID(ss[pos]) );
                pos++;
            }
        } else set[x]|=ID2BIT( L2ID(ss[pos]) );
        pos++;
    }
}

TreeElement*  parse() {
    TreeElement* root;
    int D;
    //ifstream myfile("dane.txt", ifstream::in );
	//istream myfile(cin);
    cin>>WL>>D>>N_TESTS;
   // cout<<WL<<" "<<D<<" "<<N_TESTS<<endl;
    root=new TreeElement();
    string w;
    char word[W_L];
    for (int x=0;x<D;x++) {
        cin>>w;
        const char* ww=w.c_str();
        for (int x=0;x<WL;x++) word[x]= L2ID(ww[x]);
        //cout<<w<<endl;
        root->add(word,0);
    }
    //root->printtree(0);
    unsigned long quer[W_L];
	vector<TreeElement*> r;
	r.push_back(root);
    for (int x=0;x<N_TESTS;x++) {
        cin>>w;
        //cout<<w<<endl;
        query(quer,w);
		int z=find(r,quer,0);
		cout<<"Case #"<<x+1<<":"<<setw(5)<<z<<endl;
        //const char* ww=w.c_str();
    }
    return root;
}

int main(int argc,char** argv)
{
    TreeElement *root;
    root=parse();
/*    cout<<"------------"<<endl;
	unsigned long d[W_L];
	query(d,"(dc)ac");
	for(int x=0;x<WL;x++){
	  cout<<d[x]<<" ";
	}
	cout<<endl;
	unsigned long z=root->check(d,0);
	cout<<z<<endl;
    /*for (int x=WL-1;x>=0;x--) {
        cout<<"--"<<endl;
        unsigned long s=root->filter[x];
        cout<<x<<endl;
        while (s) {
            int z=GetElement(s);
            s&=~ID2BIT(z);
            cout<<z<<" ";
        };
        cout<<endl;
    };*/
  
  
}

