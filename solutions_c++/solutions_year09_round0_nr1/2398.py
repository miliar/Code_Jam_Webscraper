#include <iostream>
#include <set>
#include <string>
#include <list>
using namespace std;

bool coincide (string &word, string &combWord) {
   int l = 0, j;
   bool esta;
   for (int i = 0; i < combWord.size(); i++) {
      if (combWord[i] != '(' && word[l] != combWord[i]) return false;
      
      else if (combWord[i] == '(') {
         esta = false;
         for (j = i+1; combWord[j] != ')'; j++) 
            if (combWord[j] == word[l]) esta = true;
         if (!esta) return false;
         i = j;
      }
      l++;
   }
      
   return true;
   
   
}

int main(int argc, char *argv[]) {
	int l, p, c;
   int count;
   string word, word2;;
   set<string> words;
   
   cin >> l >> p >> c;
   
   for (int i = 0; i < p; i++) {
      cin >> word;
      words.insert(word);
   }
   
   for (int i = 1; i <= c; i++) {
      cin >> word;
      count = 0;
      for (set<string>::iterator it = words.begin(); it != words.end(); it++) {
         word2 = *it;
         if (coincide(word2, word)) 
            count++;
      }
      cout << "Case #" << i << ": " << count << endl;
   }

   
	return 0;
}

