#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

struct node
{
  double value;
  string feature;
  node *yes;
  node *no;
};

node* parse(istringstream & stream)
{
  node* outnode = new node();
  
  //cerr << "parse called, looking for open paren" << endl;
  
  char c;
  do
  {
    stream >> c;
    //cerr << "c is " << c << endl;
  } while (c != '(');
  
  //cerr << "found open paren" << endl;
  
  //cerr << "b4 value " << outnode->value << endl;
  
  //cerr << "0peek cot char |" << stream.peek() << "|" << endl;
  stream >> outnode->value;
  stream.clear();
  //cerr << "1peek cot char |" << stream.peek() << "|" << endl;

  //cerr << "got value " << outnode->value << endl;
  
  while(1)
  {
    char d;
    stream >> d;
    stream.putback(d);
    
    // = stream.peek();
    //cerr << "peek cot char |" << d << "|" << endl;
    if(d == ' ' || d == '\n')
    {
      //cerr << "found space" << endl;
//      stream >> c;
  //    cerr << "gobbled |" << c << "|" << endl;
    }
    else if(d == ')')
    {
      //cerr << "found close paren" << endl;
      outnode->feature="";outnode->yes=0;outnode->no=0;
      return outnode;
    }
    else
    {
      //cerr << "found child" << endl;
      stream >> outnode->feature;
      //cerr << "feature " << outnode->feature << endl;
      outnode->yes = parse(stream);
      outnode->no = parse(stream);
      return outnode;
    }
  }
}
void dump (node * v)
{
  cout << "(" << v->value;
  if (v->feature != "")
  {
    cout << " " << v->feature << " ";
    dump(v->yes);
    dump(v->no);
  }
  cout << ")";
}

bool contains(vector<string> & f, string s)
{
  return (!(find(f.begin(), f.end(), s) == f.end()));
}

double find_prob(node *tree, vector<string> & features, double curprob)
{
  curprob *= tree->value;
  
  if (tree->feature == "") { return curprob; }
  
  if (contains(features, tree->feature)) { 
    return find_prob(tree->yes, features, curprob);
  }
  else {
    return find_prob(tree->no, features, curprob);
  }
}

int main()
{
  int N;
  cin >> N;
  
  for (int i=0;i<N;i++)
  {
    cout << "Case #" << i+1 << ":" << endl;
    int L;
    cin >> L;
    string dummy;
    getline(cin, dummy);
    
    string totout = "";
    
    for (int j=0;j<L;j++)
    {
      getline(cin,dummy);
      
      totout += dummy;
    }

    istringstream strm(totout);
      
    node *tree = parse(strm);
    //dump(tree);
    cout << endl;
    
    int A;
    
    cin >> A;
    
    for (int j=0;j<A; j++)
    {
      string name; cin >> name;
      int nfeat; cin >> nfeat;
      vector<string> features;
      for (int k=0; k<nfeat;k++)
      {
        string s;
        cin >> s;
        features.push_back(s);
      }
      
      double cuteprob = find_prob(tree, features, 1);
      printf("%0.7f\n", cuteprob);
    }
  }
}
