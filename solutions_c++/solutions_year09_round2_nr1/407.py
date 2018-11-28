/*
 Problem A, Round 1B, Google Code Jam 2009
   Author:   stqhmf
   Language: C++
   Method:   ad-hoc
 */

#include <cstdio>
#include <cstring>
#include <cctype>

int  def_length;
char def[100000];

double GetNumber( const int L, const int R )
{
  char buf[16];
  int  buf_length(0),i;
  for ( i=L; i<=R; ++i )
    buf[buf_length++] = def[i];
  buf[buf_length++] = def[i];
  double tmp;
  sscanf(buf,"%lf",&tmp);
  return tmp;
}

struct TreeNode
{
  double    weight;
  char      feature[32];
  TreeNode *Lchild,*Rchild;

  TreeNode( const int L, const int R ):
    Lchild(NULL),
    Rchild(NULL)
  {
    int Lweight ,Rweight;
    int Lfeature,Rfeature;
    int i,tmp;

    /*
    char ch;
    ch = def[R+1];
    def[R+1] = '\0';
    fprintf(stderr,"[[%s]]\n",def+L);
    def[R+1] = ch;
    */

    // weight, which is a real number
    for ( Lweight=L; ; ++Lweight ) 
      if ( isdigit(def[Lweight]) )
	break;
    for ( Rweight=Lweight; Rweight<=R; ++Rweight )
      if ( !isdigit(def[Rweight+1]) && def[Rweight+1]!='.' )
	break;
    this->weight = GetNumber(Lweight,Rweight);
    if ( Rweight>R ) return;

    // feature, which is a string
    for ( Lfeature=Rweight+1; Lfeature<=R; ++Lfeature )
      if ( isalpha(def[Lfeature]) )
	break;
    if ( Lfeature>R ) return;
    for ( Rfeature=Lfeature; ; ++Rfeature )
      if ( !isalpha(def[Rfeature+1]) )
	break;
    for ( i=Lfeature,tmp=0; i<=Rfeature; ++i )
      this->feature[tmp++] = def[i];
    this->feature[tmp] = '\0';

    // get left-child and right-child recursively
    int depth=0,Lbracket,Rbracket;
    for ( i=Rfeature+1; i<=R; ++i ) {
      if ( def[i]=='(' ) {
	if ( depth==0 ) Lbracket = i;
        ++depth;
      }
      else if ( def[i]==')' ) {
	--depth;
	if ( depth==0 ) {
          Rbracket = i;
	  break;
	}
      }
    }
    this->Lchild = new TreeNode(Lbracket+1,Rbracket-1);

    depth = 0;
    for ( i=Rbracket+1; i<=R; ++i ) {
      if ( def[i]=='(' ) {
        if ( depth==0 ) Lbracket = i;
        ++depth;
      }
      else if ( def[i]==')' ) {
        --depth;
	if ( depth==0 ) {
          Rbracket = i;
          break;
        }
      }
    }
    this->Rchild = new TreeNode(Lbracket+1,Rbracket-1);
  }

} *root;

struct Animal
{
  int  num_features;
  char feature[5000][16];

  Animal( char *str )
  {
    char *ptr = strtok(str," \n");
    ptr = strtok(NULL," \n");
    sscanf(ptr,"%d",&num_features);
    int i;
    for ( i=0; i<num_features; ++i ) {
      ptr = strtok(NULL," \n");
      strcpy(feature[i],ptr);
    }
  }

  bool HaveFeature( char *str )
  {
    int i;
    for ( i=0; i<num_features; ++i )
      if ( !strcmp(str,feature[i]) )
	return true;
    return false;
  }
};

void GetData()
{
  int  num_lines,i;
  char buf[5000];
  fgets(buf,sizeof(buf),stdin);
  sscanf(buf,"%d",&num_lines);

  def[0] = '\0';
  for ( i=0; i<num_lines; ++i ) {
    fgets(buf,sizeof(buf),stdin);
    strcat(buf," ");
    strcat(def,buf);
  }
}

void Parse()
{
  int i,L,R;
  def_length = strlen(def);
  for ( L=0; ; ++L )             if ( def[L]=='(' ) break;
  for ( R=def_length-1; ; --R )  if ( def[R]==')' ) break;
  root = new TreeNode(L+1,R-1);
}

void Query()
{
  int    num_queries;
  char   buf[5000],*ptr;
  double answer;
  fgets(buf,sizeof(buf),stdin);
  sscanf(buf,"%d",&num_queries);
  while ( num_queries-- ) {
    fgets(buf,sizeof(buf),stdin);
    Animal    curr_animal(buf);
    TreeNode *curr_node = root;
    answer = 1.0;
    while ( true ) {
      answer *= curr_node->weight;
      if ( curr_node->Lchild==NULL && curr_node->Rchild==NULL ) break;
      else {
        if ( curr_animal.HaveFeature( curr_node->feature ) ) curr_node = curr_node->Lchild;
        else                                                 curr_node = curr_node->Rchild;
      }
    }
    printf("%.7lf\n",answer);
  }
}

int main()
{
  int  num_cases;
  int  i;
  char buf[1024];
  fgets(buf,sizeof(buf),stdin);
  sscanf(buf,"%d",&num_cases);
  for ( i=1; i<=num_cases; ++i ) {
    printf("Case #%d:\n",i);
    GetData();
    Parse();
    Query();
  }
}
