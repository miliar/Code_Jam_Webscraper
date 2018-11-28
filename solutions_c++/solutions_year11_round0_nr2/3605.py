#include <iostream>
#include <cmath>
#include <string>
#include <cstdlib>
#include <fstream>
#include <vector>

using namespace std;

struct Elements
{
  char first, second;
};

struct Combinable
{
  Elements elements;
  char result;
};

bool check(const Elements &combine, const char &element1, const char &element2)
{
  if (((combine.first == element1) && (combine.second == element2)) ||
     ((combine.second == element1) && (combine.first == element2)))
  {
    return true;
  }
  else
    return false;
}

void eval(const string &test_case, string &answer, const vector<Combinable> &vector_c, const vector<Elements> &vector_d)
{
  int i, j, k;
  bool combined, opposed;

  for (i = 0; i < test_case.size(); ++i)
  {
    answer.push_back(test_case.at(i));
    //cout << i << "\t" << answer << endl;
    combined = opposed = false;
    if (answer.size() >= 2)
    {
      for (j = 0; j < vector_c.size(); ++j)   //check for combinable
        if (check(vector_c[j].elements, answer.at(answer.size() - 2), answer.at(answer.size() - 1)))
        {
          //cout << "\tdata " << answer.at(answer.size() - 2) << "/" << answer.at(answer.size() - 1) << endl;
          //cout << "\tcombine " << vector_c[j].elements.first << " + " << vector_c[j].elements.second;
          answer.replace(answer.size() - 2, answer.size(), &vector_c[j].result, 1);
          //cout << "\tresult " << answer << endl;
          combined = true;
          break;
        }

      if (!combined)
      {
        for (j = 0; j < vector_d.size(); ++j) //check for opposed
        {
          //cout << answer << "\t" << vector_d[j].first << vector_d[j].second << endl;
          for (k = 0; k < answer.size() - 1; ++k)
            if (check(vector_d[j], answer.at(k), answer.at(answer.size() - 1)))
            {
              //cout << "\tclear " << vector_d[j].first << " + " << vector_d[j].second << endl;
              answer.clear();
              opposed = true;
              break;
            }
          if (opposed)
            break;
        }
      }
    }
  }
}

int main(int argc, char *argv[])
{
  ifstream input("B-large.in");
  //ifstream input("teste.txt");
  ofstream output("output.txt");
  int t, n, c, d;
  vector<Combinable> vector_c;
  vector<Elements> vector_d;
  string test_case, answer;
  char temp[3];

  vector_c.reserve(36);
  vector_d.reserve(28);
  test_case.reserve(100);
  answer.reserve(100);

  int i, j, k;

  input >> t;
  for (i = 0; i < t; ++i)
  {
    vector_c.clear();
    vector_d.clear();
    test_case.clear();
    answer.clear();
    input >> c;
    for (j = 0; j < c; ++j)
    {
      input.ignore();
      input.read(temp, 3);
      vector_c.push_back(Combinable());
      vector_c[j].elements.first = temp[0];
      vector_c[j].elements.second = temp[1];
      vector_c[j].result = temp[2];
    }
    input >> d;
    for (k = 0; k < d; ++k)
    {
      input.ignore();
      input.read(temp, 2);
      vector_d.push_back(Elements());
      vector_d[k].first = temp[0];
      vector_d[k].second = temp[1];
    }
    input >> n;
    input.ignore();
    //input.getline(test_case, 100);
    getline(input, test_case);

    /*cout << test_case.at(test_case.size()) << endl;
    system("pause");*/

    eval(test_case, answer, vector_c, vector_d);
    //cout << answer << endl;
    output << "Case #" << i+1 << ": [";
    for (j = 0; j < answer.size(); ++j)
    {
      output << answer.at(j);
      if (j != answer.size() - 1)
        output << ", ";
    }
    output << "]" << endl;

    /*cout << c << " ";
    for (j = 0; j < c; ++j)
      cout << vector_c[j].elements.first << vector_c[j].elements.second << vector_c[j].result << " ";
    cout << d << " ";
    for (k = 0; k < d; ++k)
      cout << vector_d[j].first << vector_d[j].second << " ";
    cout << n << " ";
    for (j =0; j < n; ++j)
      cout << test_case[j];
    cout << endl;*/

    //system("pause");
  }


  output.close();
  input.close();
}

