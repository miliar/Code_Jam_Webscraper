#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> merge(const vector<string>& left, const vector<string>& right    );


vector<string> merge_sort(vector<string>& vec)
{
    // Termination condition: List is completely sorted if it
    // only contains a single element.
    if(vec.size() == 1)
    {
        return vec;
    }
 
    // Determine the location of the middle element in the vector
    std::vector<string>::iterator middle = vec.begin() + (vec.size() / 2);
 
    vector<string> left(vec.begin(), middle);
    vector<string> right(middle, vec.end());
 
    // Perform a merge sort on the two smaller vectors
    left = merge_sort(left);
    right = merge_sort(right);
 
    return merge(left, right);
}

vector<string> merge(const vector<string>& left, const vector<string>& right)
{
    // Fill the resultant vector with sorted results from both vectors
    vector<string> result;
    unsigned left_it = 0, right_it = 0;
 
    while(left_it < left.size() && right_it < right.size())
    {
        // If the left value is smaller than the right it goes next
        // into the resultant vector
        if(left[left_it] < right[right_it])
        {
            result.push_back(left[left_it]);
            left_it++;
        }
        else
        {
            result.push_back(right[right_it]);
            right_it++;
        }
    }
 
    // Push the remaining data from both vectors onto the resultant
    while(left_it < left.size())
    {
        result.push_back(left[left_it]);
        left_it++;
    }
 
    while(right_it < right.size())
    {
        result.push_back(right[right_it]);
        right_it++;
    }
 
    return result;
}




int main()
{
   int L,D,N;
   vector<string> words;
   string word;

   ifstream infile("A-small-attempt1.in");
   ofstream outfile("A-small-attempt1.out");

   if(infile.is_open())
   {
      infile >> L;
      infile >> D;
      infile >> N;
   }

   for (int i =0;i<D;i++)
   {
      infile >> word;

    //  cout << " okundu " << word << endl;
      words.push_back(word);
   }

   vector<string> sorted_words = merge_sort(words);

   for(int m = 0;m<N;m++)
   {
   	infile >> word;
    //    cout << " okundu denenecek " << word << endl;


   	vector<string> options;

   	int start = 0;
   	int end = 0;
   	int wordstep = 0;
   	int begin = 0;
   	int finish = 0;

   	string created="";

   	for(int i=0;i<word.length();i++)
   	{
              int eq =0;

              start = end = i;

              if(word[i]=='(')
	      {
            
                     int k;

                     for(k = i+1;k<word.length();k++)
                     {
                            if(word[k]==')') break;
                     }
            
                     end = k;
              }

              if(start == end) 
              {
                  start--;
                  end++;
                  eq = 1;
              }

                int l = 0;
                 
              for(l=start +1 ;l<end;l++)
              {
                int j=0;

         	for(;j<words.size();j++)
         	{
              		if(word[l]==words[j][wordstep]) break;
	 	}
                
          //      cout << "wordstep " << wordstep << endl;

         	if(j==words.size())
                {
                     word[l] ='-';
                     
                     if(l+1 == end && wordstep !=0)
                     {      
			begin = finish;
			finish = options.size();

	//		cout << " begin 1 " <<  begin << " finish " << finish << endl;
		    }

                }
                else
                {
             //        cout <<" wordstep " << wordstep << "letter " << word[l] << endl;
                      if(wordstep == 0)
                      {
                          created += word[l];
                          options.push_back(created);
           //               cout << "created a letter " << created << endl;
                          created = "";
                          finish++;

                      }
		      else
                      {
                          // cout <<" else wordstep " << wordstep << "letter " << word[l] << endl;

                          for(int z = begin;z<finish;z++)
                          {
                            // cout << "w";
                                 //cout <<"else + for  wordstep " << wordstep << "letter " << word[l] << endl;

 				created = options[z];
                                created += word[l];
                                // cout << " blahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" << endl;
                                if(wordstep-1)
                                {             
                                	int p = 0;
                                	for(;p<sorted_words.size();p++)
                                	{
         //                                       cout << " created " << created << " substr " << sorted_words[p].substr(0,wordstep+1) << endl;
                                                //cout << " blöhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" << endl;
                                         	if(sorted_words[p].substr(0,wordstep+1)>=created) break;
                                              // cout << " blehhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" << endl;
                                	}

                                	if(p< sorted_words.size() && sorted_words[p].substr(0,wordstep+1)==created) options.push_back(created);
       //                         	cout << "a geldim mi" << created;
                                }
                                else
                                {
                                         options.push_back(created);
                                }
                          }

                          if(l+1 == end)
                          {
                                 begin = finish;
                                 finish = options.size(); 
                                 
     //                            cout << " begin 2 " <<  begin << " finish " << finish << endl;
                          }
                      }
                }
              } 

              //begin = finish;
              //finish = options.size();
         
 	      i = end;
              if(eq) i--;
              wordstep ++;	
      }

      int count=0;

      for(int i=0;i<options.size();i++)
      {
        for(int j=0;j<sorted_words.size();j++)
        {
             //cout << options[i] << endl;
             if(options[i]==sorted_words[j])
             {
                   count++;
                   break;
             }
        }
     }


     outfile << "Case #" << m+1 << ": " << count << endl;
     
    options.empty();
    wordstep = 0;
  }
  
   return 0;
}
