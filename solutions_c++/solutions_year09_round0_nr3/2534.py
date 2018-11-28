#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;

const char* LETTER_SET = "welcom tdja";
const char* LETTER_SQU = "welcome to code jam";

class Data {
 public:
  Data(char character, int counter, int position) : ch(character), count(counter), pos(position) {};
  char ch;
  int count;
  int pos;
};

int calcData(vector<Data>& currdataLst, vector<Data>& newdataLst, vector<int> chLst) {
    for (std::vector<int>::iterator it = chLst.begin(); it!=chLst.end(); ++it) {
      int counter = 0;
      for (std::vector<Data>::iterator dataIt = currdataLst.begin(); dataIt!=currdataLst.end(); ++dataIt) {
        if (dataIt->pos < *it) {
          counter += dataIt->count;
        }
      }
      Data data('x', counter, *it);
      newdataLst.push_back(data);
    }
    return newdataLst.size();
}

void printResult(int n, int result)
{
  printf("Case #%d: %4,0d\n", n, result);
}

int main(int argc, const char *argv[])
{
  //freopen("A-small-attempt0.in", "r", stdin);
  //freopen("output.txt", "w", stdout);
  int N; //Number of test case

  int i, j, k, l, m, n;
  scanf("%d\n", &N);
  for (i = 0; i < N; i++) {
    int result = 0;
    char* input = new char[502];
    input[0] = 0;
    char* trimedInput = new char[502];
    trimedInput[0] = 0;
    std::vector<int> wlist;
    std::vector<int> elist;
    std::vector<int> llist;
    std::vector<int> clist;
    std::vector<int> olist;
    std::vector<int> mlist;
    std::vector<int> _list;
    std::vector<int> tlist;
    std::vector<int> dlist;
    std::vector<int> jlist;
    std::vector<int> alist;


    scanf("%[^\n]\n", input);

    //printf("Input::%s\n", input);

    //Trim input
    int index = 0;
    bool started = false;
    int lastM = -1;
    for (j = 0; j < strlen(input); j++) {
      if (started || input[j] == 'w') {
        started = true;
        if (strrchr(LETTER_SET, input[j]) != NULL) {
          if (input[j] == 'm') {
            lastM = index;
          }
          trimedInput[index++] = input[j];
        }
      }
    }
    trimedInput[index++] = 0;
    //printf("TrimedInput1::%s\n", trimedInput);
    if (lastM == -1) {
      printResult(i+1, 0);
      continue;
    } else {
      trimedInput[lastM+1] = 0;
    }

    for (j = 0; j < strlen(trimedInput); j++) {
      switch (trimedInput[j]) {
        case 'w':
          wlist.push_back(j);
          break;
        case 'e':
          elist.push_back(j);
          break;
        case 'l':
          llist.push_back(j);
          break;
        case 'c':
          clist.push_back(j);
          break;
        case 'o':
          olist.push_back(j);
          break;
        case 'm':
          mlist.push_back(j);
          break;
        case ' ':
          _list.push_back(j);
          break;
        case 't':
          tlist.push_back(j);
          break;
        case 'd':
          dlist.push_back(j);
          break;
        case 'j':
          jlist.push_back(j);
          break;
        case 'a':
          alist.push_back(j);
          break;
        default:
          printf("Unknown char::%c", trimedInput[j]);
      }
    }

    //Calc
    std::vector<Data>* currdataLst = new std::vector<Data>();
    std::vector<Data>* newdataLst = new std::vector<Data>();

    //w
    for (std::vector<int>::iterator it = wlist.begin(); it!=wlist.end(); ++it) {
      Data data('w', 1, *it);
      currdataLst->push_back(data);
    }
    if (currdataLst->size()==0) {
      printResult(i+1, 0);
      continue;
    }

    //e
    if (calcData(*currdataLst, *newdataLst, elist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }

    //l
    if (calcData(*currdataLst, *newdataLst, llist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    
    //c
    if (calcData(*currdataLst, *newdataLst, clist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    
    //o
    if (calcData(*currdataLst, *newdataLst, olist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //m
    if (calcData(*currdataLst, *newdataLst, mlist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //e
    if (calcData(*currdataLst, *newdataLst, elist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //_
    if (calcData(*currdataLst, *newdataLst, _list)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //t
    if (calcData(*currdataLst, *newdataLst, tlist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //o
    if (calcData(*currdataLst, *newdataLst, olist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //_
    if (calcData(*currdataLst, *newdataLst, _list)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //c
    if (calcData(*currdataLst, *newdataLst, clist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //o
    if (calcData(*currdataLst, *newdataLst, olist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //d
    if (calcData(*currdataLst, *newdataLst, dlist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //e
    if (calcData(*currdataLst, *newdataLst, elist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //_
    if (calcData(*currdataLst, *newdataLst, _list)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //j
    if (calcData(*currdataLst, *newdataLst, jlist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //a
    if (calcData(*currdataLst, *newdataLst, alist)==0) {
      printResult(i+1, 0);
      continue;
    }
    else
    {
      delete currdataLst;
      currdataLst = newdataLst;
      newdataLst = new std::vector<Data>();
    }
    //m
    if (calcData(*currdataLst, *newdataLst, mlist)==0) {
      printResult(i+1, 0);
    }
    else
    {
      int counter=0;
      for (vector<Data>::iterator dataIt = newdataLst->begin(); dataIt!=newdataLst->end(); ++dataIt) {
        counter += dataIt->count;
      }
      printResult(i+1, counter%10000);
    }

  }

  return 0;
}
