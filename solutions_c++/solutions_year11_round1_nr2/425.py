#include<stdio.h>
#include<string>
#include<math.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>

using namespace std;

int maxWrong;
string maxWrongWord;
int maxWordInd;
char guess[100];
vector<string> words;

void dfs(vector<int> wordInds, int wrong, int deep, vector<char> leftGuess)
{
    vector<int> nextWordInds;
    vector<int> nextYesWordInds, nextNoWordInds;
    char nowGuess;
    vector<char> nowLeftGuess, nextGuess;
    bool used[10005];
    int i, j, k;

    if (deep == 0) {
        for (i = 0; i < wordInds.size(); i ++) {
            used[i] = false;
        }

        for (i = 0; i < wordInds.size(); i ++) {
            if (used[i])
                continue;

            nextWordInds.clear();
            for (j = i; j < wordInds.size(); j ++) {
                if (used[j])
                    continue;
                if (words[wordInds[i]].length() == words[wordInds[j]].length()) {
                    used[j] = true;
                    nextWordInds.push_back(j);
                }
            }

            nextGuess.clear();

            dfs(nextWordInds, wrong, deep+1, leftGuess);
        }

        return;
    }

    if (wordInds.size() == 1) {
        if (wrong > maxWrong) {
            maxWrong = wrong;
            maxWrongWord = words[wordInds[0]];
            maxWordInd = wordInds[0];
        }
        else if (wrong == maxWrong && wordInds[0] < maxWordInd) {
            maxWrongWord = words[wordInds[0]];
            maxWordInd = wordInds[0];
        }

        return;
    }
    if (wordInds.size() == 0)
        return;

    for (i = 0; i < 300; i ++) {
        used[i] = false;
    }
    for (i = 0; i < wordInds.size(); i ++) {
        for (j = 0; j < words[wordInds[i]].length(); j ++) {
            used[words[wordInds[i]][j]] = true;
        }
    }
    nowLeftGuess.clear();
    for (i = 0; i < leftGuess.size(); i ++) {
        if (used[leftGuess[i]])
            nowLeftGuess.push_back(leftGuess[i]);
    }
        
    nowGuess = nowLeftGuess[0];
    nextGuess.clear();
    for (i = 1; i < leftGuess.size(); i ++) {
        nextGuess.push_back(leftGuess[i]);
    }    
    //category
    for (i = 0; i < wordInds.size(); i ++) {
        for (j = 0; j < words[wordInds[i]].length(); j ++) {
            if (words[wordInds[i]][j] == nowGuess) {
                nextYesWordInds.push_back(wordInds[i]);
                break;
            }
        }
        if (j >= words[wordInds[i]].length())
            nextNoWordInds.push_back(wordInds[i]);
    }

    //yes
    for (i = 0; i < nextYesWordInds.size(); i ++) {
        used[i] = false;
    }
    for (i = 0; i < nextYesWordInds.size(); i ++) {
        if (used[i])
            continue;

        nextWordInds.clear();
        for (j = i; j < nextYesWordInds.size(); j ++) {
            if (used[j])
                continue;

            for (k = 0; k < words[nextYesWordInds[i]].length(); k ++) {
                if (words[nextYesWordInds[i]][k] == nowGuess && words[nextYesWordInds[j]][k] != nowGuess)
                    break;
                if (words[nextYesWordInds[i]][k] != nowGuess && words[nextYesWordInds[j]][k] == nowGuess)
                    break;
            }
            if (k >= words[nextYesWordInds[i]].length()) {
                used[j] = true;
                nextWordInds.push_back(nextYesWordInds[j]);
            }
        }

        dfs(nextWordInds, wrong, deep+1, nextGuess);
    }

    //no
    dfs(nextNoWordInds, wrong+1, deep+1, nextGuess);
}

int main()
{
    int i, j, k;
    int t, nowt;
    int n, m;
    char word[1000000];
    vector<int> wordInds;
    vector<char> nextGuess;

    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);


    scanf("%d", &t);
    nowt = 0;
    while (t --) {
        nowt ++;
        scanf("%d%d", &n, &m);
        words.clear();
        wordInds.clear();
        for (i = 0; i < n; i ++) {
            scanf("%s", word);
            words.push_back(word);
            wordInds.push_back(i);
        }
        printf("Case #%d:", nowt);
        for (i = 0; i < m; i ++) {
            maxWrong = -1;
            scanf("%s", guess);
            nextGuess.clear();
            for (j = 0; j < strlen(guess); j ++) {
                nextGuess.push_back(guess[j]);
            }
            dfs(wordInds, 0, 0, nextGuess);
            printf(" %s", maxWrongWord.c_str());
        }
        printf("\n");
    }

    return 0;
}