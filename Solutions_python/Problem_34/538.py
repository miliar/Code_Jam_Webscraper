import re
arquivo = open('E:\\Documents and Settings\\ikke\\Desktop\\codejam\\A-large.in','r')
saida = open('A-large.out','w')

tamanho, quantidade, regexes = [int(x) for x in arquivo.readline().split()]


palavras = "".join(arquivo.readline() for x in range(quantidade))


for x in range(regexes):
    alienregex = arquivo.readline().replace('(','[').replace(')',']{1}')
    alienregex = re.compile(alienregex)

    saida.write('Case #%i: %i\n' % (x+1, len(alienregex.findall(palavras))))

arquivo.close()
saida.close()
