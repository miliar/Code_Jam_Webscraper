#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool find(char c, string str);
bool compare(string str1, string str2);//abc,(ab)(bc)(ca)

int main()
{
    int L,D,N;
    cin >> L >> D >> N;
    vector<string> v, v1;
    string str;
    for (int i=0; i<D; i++)
    {
        cin >> str;
        v.push_back(str);
    }
    for (int i=0; i<N; i++)//v1 is test case
    {
        cin >> str;
        v1.push_back(str);
    }
    int num;
    int flag = false;
    int n;
    for (int i=0; i<N; i++)//(ab)(bc)(ca) v1
    {
        num = 0;
        n = i+1;
        for (int j=0; j<D; j++)//abc v
        {
            flag = compare(v[j], v1[i]);
            if (flag == true) num++;
        }
        cout << "Case #" << n << ": " << num << endl;
    }
    system("pause");
    return 0;
}

bool compare(string str1, string str2)//abc,(ab)(bc)(ca)
{
    int len1 = str1.length();
    int len2 = str2.length();
    string strtmp;
    char c1,c2;
    bool flag = false;
    int i= 0, j=0;
    while (i<len1)
    {
        c1 = str1[i];
        flag = false;

        strtmp.clear();
        if (j<len2)//�ж��Ƿ�ƥ��
        {
            c2 = str2[j];
            if (c2=='(') //������
            {
                j++;
                while (str2[j]!=')')//���������ݱ�������
                {
                    strtmp += str2[j];
                    j++;
                }
                j++;//ָ����������һ���ַ�
                flag = find(c1, strtmp);
            }
            else//������
            {
                if (str2[j] == c1) flag = true;
                j++;
            }
        }
        if (flag == false) break; //ƥ�䲻�ɹ�
        i++;
    }

    if (i == len1) return true;
    else return false;
}

bool find(char c, string str)//����c�Ƿ���str�У��ɹ�����true
{
    int len = str.length();
    for (int i=0; i<len; i++)
    {
        if (c == str[i]) return true;
    }
    return false;
}
