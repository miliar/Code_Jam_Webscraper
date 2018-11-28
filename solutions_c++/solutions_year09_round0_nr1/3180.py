#include <iostream>
#include <fstream>
#include <ostream>
#include <istream>
#include <set>
#include <stdlib.h>
#include <string>
#include <vector>

typedef struct CharNodeStruct {
  CharNodeStruct* chars[26];
} CharNode;

int main(int argc, char** argv){

  if(argc != 2){
    std::cerr << "Error: Invalid arguments" << std::endl;
    return EXIT_FAILURE;
  }

  std::string filename = argv[1];
  std::string fileline;

  std::ifstream datafile(filename.c_str());
  if(!datafile.is_open()){
    std::cerr << "Error: Unable to open file" << std::endl;
    return EXIT_FAILURE;
  }

//   std::cerr << "Retrieving intial arguments" << std::endl;
  int L, D, N;
  datafile >> L >> D >> N;
//   std::cerr << "L: " << L << ", D: " << D << ", N: " << N << std::endl;
  getline(datafile, fileline);

  // Word Array
  bool** word_array = new bool*[L];
  for(int i = 0; i < L; i++){
    word_array[i] = new bool[26];
  }

  CharNode* dict_root = new CharNode();
  for(int i = 0; i < 26; i++)
    dict_root->chars[i] = NULL;

  // Create a tree representing the letters in the possible word graph
  std::vector<int> temp_depth;
  for(int i = 0; i < D; i++){
    temp_depth.clear();
    getline(datafile, fileline);
//     std::cerr << i << ": '" << fileline << "'" << std::endl;
    
    CharNode* traverse_ptr = dict_root;
    for(int j = 0; j < fileline.size(); j++){
      if(traverse_ptr->chars[(int)fileline[j] - 'a'] == NULL){
        traverse_ptr->chars[(int)fileline[j] - 'a'] = new CharNode();
        for(int k = 0; k < 26; k++)
          (traverse_ptr->chars[(int)fileline[j] - 'a'])->chars[k] = NULL;
      }
      traverse_ptr = traverse_ptr->chars[(int)fileline[j] - 'a'];
      temp_depth.push_back((int)fileline[j] - 'a');
    }
//     for(int i = 0; i < temp_depth.size(); i++)
//       std::cerr << temp_depth[i];
//     std::cerr << std::endl;
  }

//   std::cerr << "Tree completed" << std::endl;

  int* index_at_depth = new int[L];
  CharNode** parent_at_depth = new CharNode*[L];

  for(int k = 0; k < N; k++){
    int filelineCounter = 0;

    getline(datafile, fileline);

    for(int i = 0; i < L; i++)
      for(int j = 0; j < 26; j++)
        word_array[i][j] = false;

    // Load word possibilities into boolean array
    for(int i = 0; i < L; i++, filelineCounter++){
      if(fileline[filelineCounter] == '('){
        filelineCounter++;
        for(; fileline[filelineCounter] != ')'; filelineCounter++){
          word_array[i][(int)fileline[filelineCounter] - 'a'] = true;
//           std::cerr << "word_array[" << i << "][" 
//                     << (int)fileline[filelineCounter] - 'a'
//                     << "]=true" << std::endl;
         
        }
      }
      else{
        word_array[i][(int)fileline[filelineCounter] - 'a'] = true;
//         std::cerr << "word_array[" << i << "][" 
//                   << (int)fileline[filelineCounter] - 'a'
//                   << "]=true" << std::endl;
      }
    }

//     std::cerr << "Array for " << fileline << " completed" << std::endl;

    int word_count = 0;

    for(int i = 0; i < L; i++)
      index_at_depth[i] = 0;
    //parent_at_depth[0] = NULL;

    CharNode* traverse_ptr = dict_root;
    int depth = 0;
    while(depth >= 0){
//       std::cerr << "Depth: " << depth << ", IatD: " 
//                 << index_at_depth[depth] << std::endl;
//       if(depth == L){
//         for(int i = 0; i < 26; i++)
//           if(traverse_ptr->chars[i] != NULL && word_array[depth][i] == true){
//             word_count++;
//             std::cerr << "word_count++ @ ";
//             for(int x = 0; x <= depth; x++){
//               std::cerr << "->" << index_at_depth[x];
//             }
//             std::cerr << "->" << i << std::endl;
//           }
//          word_count++;
//          std::cerr << "word_count++ @ ";
//          for(int x = 0; x <= depth; x++){
//            std::cerr << "->" << index_at_depth[x];
//          }
//          std::cerr << std::endl;
//          traverse_ptr = parent_at_depth[depth--];
//          index_at_depth[depth]++;
//       }
//       else{
        if( ! (index_at_depth[depth] < 26)){
          traverse_ptr = parent_at_depth[depth--];
          index_at_depth[depth]++;
        }
        else if(traverse_ptr->chars[index_at_depth[depth]] != NULL
                && word_array[depth][index_at_depth[depth]] == true)
        {
          if(depth == L-1){
            word_count++;

//             std::cerr << "word_count++ @ ";
//             for(int x = 0; x <= depth; x++){
//               std::cerr << "->" << index_at_depth[x];
//             }
//             std::cerr << std::endl;

            index_at_depth[depth]++;
          }
          else{
            parent_at_depth[depth+1] = traverse_ptr;
            index_at_depth[depth+1] = 0;
            traverse_ptr = traverse_ptr->chars[index_at_depth[depth]];
            depth++;
          }
        }
        else index_at_depth[depth]++;
        //}

//      getchar();
    }

    std::cout << "Case #" << k+1 << ": " << word_count << std::endl;
  }

  for(int i = 0; i < L; i++)
    delete[] word_array[i];

  delete[] word_array;
  //delete[] word_array_size;
  //delete[] word_array_counter;
  delete[] index_at_depth;
}
