#include <iostream>

using namespace std;

const int MAX_LETTERS = 26;

int word_length;
int num_words;
int num_cases;
int num_matches;

struct token {
  int num_letters;
  char letters[MAX_LETTERS];
};

struct tree_node {
  char letter;
  struct tree_node* children[MAX_LETTERS];
};


void add_word(struct tree_node *root, const char* word) {
  struct tree_node *current_node = root;
  for (int i = 0; i < word_length; i++) {
    if (current_node->children[word[i] - 'a'] != NULL)
      current_node = current_node->children[word[i] - 'a'];
    else {
      struct tree_node* new_node = new struct tree_node();
      new_node->letter = word[i];
      for(int child = 0; child < MAX_LETTERS; child++)
        new_node->children[child] = NULL;
      current_node->children[word[i] - 'a'] = new_node;
      current_node = new_node;
    }
  }
}


void search_word(const struct tree_node *node, const token *tokens, const int index) {
  if (index == word_length) {
    num_matches++;
    return;
  }
  for (int i = 0; i < tokens[index].num_letters; i++) {
    char letter = tokens[index].letters[i];
    if (node->children[letter - 'a']) {
      search_word(node->children[letter - 'a'], tokens, index + 1);
    }
  }
}


main() {
  struct tree_node *root = new struct tree_node();
  char line[512];
  for (int child = 0; child < MAX_LETTERS; child++)
    root->children[child] = NULL;
  cin >> word_length >> num_words >> num_cases;
  for (int i = 0; i < num_words;) {
    cin.getline(line, word_length + 1);
    if (line[0] == '\0')
      continue;
    add_word(root, line);
    i++;
  }
  for (int test_case = 1; test_case <= num_cases; test_case++) {
    int curr_token = -1, curr_letter = 0;
    bool in_token = false, advance = true;
    token test_tokens[15];
    num_matches = 0;
    cin.getline(line, 512);
    while (line[curr_letter] != '\0') {
      if (advance) {
        advance = false;
        curr_token++;
        test_tokens[curr_token].num_letters = 0;
      }
      if (line[curr_letter] == '(')
        in_token = true;
      else if (line[curr_letter] == ')') {
        in_token = false;
        advance = true;
      } else {
        test_tokens[curr_token].letters[test_tokens[curr_token].num_letters++] = line[curr_letter];
        if (!in_token)
          advance = true;
      }
      curr_letter++;
    }
    if (curr_token != word_length - 1) {
      num_matches = 0;
    } else 
      search_word(root, test_tokens, 0);
    cout << "Case #" << test_case << ": " << num_matches << endl;
  }
}


