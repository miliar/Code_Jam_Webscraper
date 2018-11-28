#include <iostream>
#include <vector>
#include <string>

class node
{
public:
   node() { memset(entries, 0, sizeof(entries)); }
   ~node() { for (int i = 0; i < 26; i++) delete entries[i]; }
   node *entries[26];
};

class tree
{
   public:
      tree() { root = new node; }
      ~tree() {  delete root; }
      void insert (std::string &s)
      {
         int pos;
         node *p = root;
         for (int j = 0; j < s.length(); j++)
         {
            pos = s[j] - 'a'; // Don't throw EBCDIC at this one
            if (p->entries[pos] == NULL)
               p->entries[pos] = new node;
            p = p->entries[pos];
         }
      }
      
      int find (std::vector < std::string > & sv)
      {
         return find (sv, 0, root);
      }

   private:
      node *root;

      int find (std::vector < std::string > &sv, size_t pos, node *p)
      {
         int val = 0;
         if (sv.size() - pos == 0) return 1;
         for(int i = 0; i < sv[pos].length(); i++)
            if (p->entries[sv[pos][i] - 'a'])
               val += find(sv, pos + 1, p->entries[sv[pos][i] - 'a']);
         return val;
      }
};



int main(void)
{
   int L, D, N;
   tree t;

   // input the parameters
   std::cin >> L >> D >> N;
   std::cin.ignore(256, '\n');

   // read the dictionary of known words and store in parse tree
   std::string s;
   for (int i = 0; i < D; i++)
   {
      getline(std::cin, s);
      t.insert(s);
   }

   std::vector < std::string > sv;
   sv.reserve(L);
    
   // Read each test case, construct vectors of strings of possible characters at each position,
   // and try to find all possibilities in the parse tree
   for (int testnum = 1; testnum <= N; testnum++)
   {
      std::string s;
      getline(std::cin, s); 
      size_t begin = 0, end = 0;
      for (int pos = 0; pos < L; pos++)
      {
          if (s[begin] != '(') sv.push_back(std::string(1, s[begin++])); 
          else {begin++; end = s.find_first_of( ')', begin); 
             sv.push_back(std::string(s, begin, end-begin));begin = end + 1;}
      } 
      std::cout << "Case #" << testnum << ": " << t.find(sv) << std::endl;
      sv.clear();
   }
}
