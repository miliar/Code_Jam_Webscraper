#include<iostream>
#include<iomanip>
#include<cassert>
#include<vector>
#include<tr1/unordered_set>
#include<string>

struct Tree
{
  double w;
  std::string feature;
  Tree* left;
  Tree* right;
  Tree(double w)
  {
    this->w = w;
    left = right = 0;
  }
  Tree (double ww,std::string f,Tree* l,Tree* r)
  {
    w = ww;
    feature = f;
    left = l;
    right = r;
  }
  bool is_leaf()
  {
    return left==0;
  }
};

Tree* parse(std::istream& in)
{
  char c=0;

  while(c!='(')
  {
    //if(c!=0)
      //std::cout<<"c="<<c<<"\n";;
    in>>c;
  }

  double w;
  in>>w;
  //std::cout<<"w="<<w<<"\n";
  in>>c;
  while(isspace(c))
    in>>c;
  if(c==')')
  {
    return new Tree(w);
  }
  std::string f;
  f.push_back(c);
  c = 0;
  while(!isspace(in.peek()) && in.peek()!='(')
  {
    in>>c;
    f.push_back(c);
  }
  Tree* l = parse(in);
  Tree* r = parse(in);
  c = 0;
  while(c!=')')
  {
    in>>c;
  }
  return new Tree(w,f,l,r);
}
void print_tree(Tree* t)
{
  std::cout<<"(";
  std::cout<<t->w;
  if(!t->is_leaf())
  {
    std::cout<<" "<<t->feature<<" ";
    print_tree(t->left);
    std::cout<<" ";
    print_tree(t->right);
  }
  std::cout<<")";
}
struct Animal
{
  std::tr1::unordered_set<std::string> feats;
  std::string name;
};


double prob(Tree* t,Animal& a)
{
  if(t->is_leaf())return t->w;
  if(a.feats.count(t->feature))
  {
    return t->w*prob(t->left,a);
  }else{
    return t->w*prob(t->right,a);
  }
}

void handle_case(int case_no)
{
  int n=0;
  while(isspace(std::cin.peek()))std::cin.get();
  //std::cout<<"peek = "<<(char)std::cin.peek()<<"\n";
  std::cin>>n;
  //std::cout<<"n = "<<n<<"\n";
  Tree* t = parse(std::cin);
  std::cin>>n;
  //print_tree(t);
  //print_tree(t);
  std::vector<Animal> animals;
  for(int i=0;i<n;i++)
  {
    Animal a;
    std::cin>>a.name;
    int fn = 0;
    std::cin>>fn;
    for(int j=0;j<fn;j++)
    {
      std::string feat;
      std::cin>>feat;
      a.feats.insert(feat);

    }
    animals.push_back(a);
  }
  std::cout<<"Case #"<<case_no<<":\n";
  assert(n==animals.size());
  for(int i=0;i<n;i++)
  {
    //std::cout<<animals[i].name<<":";
    std::cout<<std::fixed<<std::setprecision(7)<<prob(t,animals[i])<<"\n";;
  }
}

int main() {
  int n;
  std::cin>>n;
  for(int i=0;i<n;i++)
  {
    handle_case(i+1);
  }

}
