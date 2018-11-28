using namespace std;
#import <iostream>
#import <string>
#import <map>

struct node
{
   float w;
   bool leaf;
   string feature;
   struct node *yes;
   struct node *no;
};


typedef struct node * tnode;

char temp[12];

tnode read_node()
{
   char ct;
   scanf(" %c ", &ct); // read '('
   
   tnode nd;
   nd = new struct node;
   scanf(" %f ", &(nd->w)); // get weight
   
   scanf(" %c ", &ct);
   if (ct == ')')
   {
      nd->leaf = true;
   }
   else
   {
      nd->leaf = false;
      temp[0] = ct;
      temp[1] = '\0';
      scanf(" %[a-z]s ", temp+1);
      string nm (temp);
      nd->feature = nm;
      nd->yes = read_node();
      nd->no = read_node();
      scanf(" %c ", &ct); // get ')' finally
   }
   return nd;
}

int main()
{
   int t; // number of test cases
   cin >> t;
   int c = 0;
   while (c++ < t)
   {
      cout << "Case #" << c << ":" << endl;
   
      int l; // number of lines of the tree
      cin >> l; // useless
      
      tnode root = read_node();
      
      int a; // number of animals
      cin >> a;
      while (a--)
      {
         string nm;
         cin >> nm; // animal name
         int n; // number of features
         cin >> n;
         map<string, bool> features;
         for (int i = 0; i < n; ++i) // read the features
         {
            string ft;
            cin >> ft; // feature name
            features[ft] = true;
         }
         
         float p = 1;
         tnode curr = root;
         while (true)
         {
            p *= curr->w;
            if (curr->leaf) break;
            if (features[curr->feature])
               curr = curr->yes;
            else
               curr = curr->no;
         }
         printf("%.7f\n", p);
      }
   }
   return 0;
}
