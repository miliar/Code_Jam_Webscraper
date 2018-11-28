
#include <stdio.h>
#include <map>


class CRemover{
public:
	CRemover()
	{
		memset(m_checkTable, 0, sizeof(int)*26);
	}

	bool tick(char elem)
	{
		if(m_checkTable[elem-'A']>0)
		{
			return true;
		}

		for( const char* pStr = m_removeTable[elem-'A'].c_str() ; *pStr ; pStr++)
		{
			m_checkTable[(*pStr) - 'A']++;
		}

		return false;
	}

	void untick(char elem)
	{
		for( const char* pStr = m_removeTable[elem-'A'].c_str() ; *pStr ; pStr++)
		{
			m_checkTable[(*pStr) - 'A']--;

			if(m_checkTable[(*pStr) - 'A']<0)
			{
				printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
				printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
				printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
			}
		}


	}

	void resetTick()
	{
		memset(m_checkTable, 0, sizeof(int)*26);
	}

	void addRemovePair(char elem1, char elem2)
	{
		if(elem1 == elem2)
		{
			m_removeTable[elem1-'A'].append(1, elem2);
		}
		else
		{
			m_removeTable[elem1-'A'].append(1, elem2);
			m_removeTable[elem2-'A'].append(1, elem1);
		}
		
	}

private:
	std::string m_removeTable[26];
	int m_checkTable[26];
};

class CCombiner{
public:
	CCombiner(){
		memset(m_map, 0 , sizeof(char)*26*26);
	}

	void addPair(char elem1, char elem2, char targetElem)
	{
		m_map[getIndex(elem1, elem2)] = targetElem;
		m_map[getIndex(elem2, elem1)] = targetElem;
	}

	char Combine(char elem1, char elem2)
	{
		return m_map[getIndex(elem1, elem2)];
	}
private:

	int getIndex(char elem1, char elem2)
	{
		return (elem1 - 'A')*26 + elem2 - 'A';
	}

	char m_map[26*26];

};
class CElementList{
public:
	CElementList(CCombiner *pCombiner, CRemover *pRemover)
		: m_count(0)
		, m_pCombiner(pCombiner)
		, m_pRemover(pRemover)
	{
		memset(m_element, 0, sizeof(char)*100);
	}

	void add(char elem)
	{

		if(m_count>0)
		{
			char toChar = m_pCombiner->Combine(elem, m_element[m_count-1]);

			if(toChar)
			{
				m_pRemover->untick(m_element[m_count-1]);
				replaceLastElement(toChar);
				return;
			}
		}
		

		// check remover
		if(m_pRemover->tick(elem))
		{
			clearElementArray();
			m_pRemover->resetTick();
			return;
		}

		addElementArray(elem);
	}

	int getCount(){return m_count;}
	const char* getElementArray(){return &m_element[0];}
private:

	void addElementArray(char elem)
	{
		m_element[m_count++] = elem;
	}

	void replaceLastElement(char elem)
	{
		m_element[m_count-1] = elem;
	}

	void clearElementArray()
	{
		m_count = 0;
		m_element[0]=0;
	}

	CCombiner *m_pCombiner;
	CRemover  *m_pRemover;
	int m_count;
	char m_element[100];

};
int main(int argc, char* argv[])
{

	freopen("c:\\input.in","r",stdin);
	freopen("C:\\output.txt","w",stdout);

	int T = 0;

	scanf("%d", &T);

	for(int t = 0 ; t < T ; t++)
	{
		CCombiner combiner;
		CRemover remover;
		CElementList result(&combiner, &remover);

		int combineNum;
		scanf("%d", &combineNum);
		if(combineNum>0)
		{
			for(int c = 0 ; c < combineNum ; c++)
			{
				char combinestr[4];
				scanf("%s", combinestr);
				combiner.addPair(combinestr[0], combinestr[1], combinestr[2]);
			}
		}


		int removeNum;
		scanf("%d", &removeNum);
		if(removeNum>0)
		{
			for(int r = 0 ; r < removeNum ;r ++)
			{
				char removestr[3];
				scanf("%s", removestr);
				remover.addRemovePair(removestr[0], removestr[1]);
			}
		}

		int N;
		scanf("%d", &N);

		char inputElemArray[101];
		scanf("%s", inputElemArray);

		for(int n = 0 ; n < N ; n++)
		{
			result.add(inputElemArray[n]);
		}

		printf("Case #%d: ", t+1);
		printf("[");
		int retCount = result.getCount();
		const char* pRetElem = result.getElementArray();
		for(int ret = 0 ; ret < retCount ; ret++)
		{
			if(ret !=0)
				printf(", %c", pRetElem[ret]);
			else
				printf("%c", pRetElem[ret]);
			
		}
		printf("]\n");

//		printf("Case #%d: %d\n", t+1, timeCur);
	}

	return 0;
}