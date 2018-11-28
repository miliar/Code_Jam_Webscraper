#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <ctype.h>
#include <assert.h>

// for each letter/index, in which words it appears
std::vector< std::vector<int> > g_vecLUT;

void GetLine(std::string *pOut) {
	pOut->reserve(4096); // should probably be enough
	char c;
	while (1) {
		*pOut = "";
		while (!std::cin.eof() && (c = std::cin.get()) != '\n') {
			*pOut += c;
		}
		for (int i = 0; i < (int)pOut->size(); ++i)
			if (!isspace((*pOut)[i]))
				return;
	}
}

const char *GetToken(const char *p, std::vector<char> * const pToken) {
	if (islower(*p)) {
		pToken->push_back(*p);
		return p + 1;
	} else if (*p == '(') {
		while (*++p != ')') {
			assert(islower(*p));
			pToken->push_back(*p);
		}
		return p + 1;
	} else
		abort();
}

void GetGarbled(std::vector< std::vector<char> > * const pGarbled) {
	std::string str;
	GetLine(&str);
	const char * const sz = str.c_str();
	pGarbled->reserve(str.size());
	const char *p = sz;
	while (*p != '\0') {
		pGarbled->resize(pGarbled->size() + 1);
		p = GetToken(p, &*pGarbled->rbegin());
	}
}

int CountPossibleWords
    (std::vector< std::vector<char> > * const pGarbled,
     const std::vector<std::string> * const pWordsVec)
{
	int i;
	std::vector<int> vecCounts(pWordsVec->size(), 0);
	for (i = 0; i < (int)pGarbled->size(); ++i) {
		std::vector<char> * const pToken = &(*pGarbled)[i];
		int j;
		std::vector<std::string> vecNewWords;
		for (j = 0; j < (int)pToken->size(); ++j) {
			std::vector<int> *p = &g_vecLUT[((*pToken)[j] - 'a') + i * 26];
			std::vector<int>::iterator it;
			for (it = p->begin(); it != p->end(); ++it)
				++vecCounts[*it];
// 			for (k = 0; k < (int)vecWords.size(); ++k) {
// 				if ((*pToken)[j] == vecWords[k][i]) {
// 					vecNewWords.push_back(vecWords[k]);
// 				}
// 			}
		}
	}
	int nRet = 0;
	for (i = 0; i < (int)vecCounts.size(); ++i)
		if (vecCounts[i] == (int)pGarbled->size())
			++nRet;
	return nRet;
// 	std::cerr << "Matched words are: ";
// 	for (int i = 0; i < (int) vecWords.size(); ++i) {
// 		std::cerr << vecWords[i] << " ";
// 	}
// 	std::cerr << "\n";
// 	for (i = 0; i < (int)pGarbled->size(); ++i) {
// 		nTotalWords *= (*pGarbled)[i].size();
// 	}
// 	for (nWordIndex = 0; nWordIndex < nTotalWords; ++nWordIndex) {
// 		std::string str = ""; str.reserve(pGarbled->size());
// 		int nProd = 1;
// 		for (i = 0; i < (int)pGarbled->size(); ++i) {
// 			str += (*pGarbled)[i][nWordIndex / nProd % (*pGarbled)[i].size()];
// 			nProd *= (*pGarbled)[i].size();
// 		}
// //		std::cerr << "To cerr: " << str << "\n";
// 		if (pWords->find(str) != pWords->end())
// 			++nPossibleWords;
// 	}
// 	return nPossibleWords;
}


int main() {
	int nWordSize, nWordCount, nGarbledCount, i;
	std::cin >> nWordSize;
	std::cin >> nWordCount;
	std::cin >> nGarbledCount;
	std::vector<std::string> vecWords;
	g_vecLUT.resize(nWordSize * 26);
	for (i = 0; i < nWordCount; ++i) {
		std::string str;
		GetLine(&str);
		vecWords.push_back(str);
		for (int j = 0; j < (int)str.size(); ++j) {
			g_vecLUT[j * 26 + (str[j] - 'a')].push_back(i);
		}
	}
	for (i = 0; i < nGarbledCount; ++i) {
		std::vector< std::vector<char> > vecGarbled;
		GetGarbled(&vecGarbled);
		std::cout 
		    << "Case #" 
		    << (i + 1) 
		    << ": " 
		    << CountPossibleWords(&vecGarbled, &vecWords) << "\n";
	}

}
