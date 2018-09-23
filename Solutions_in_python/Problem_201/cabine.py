
def cabineFinal():
	texto = lêEntrada()
	while texto != "":
		T, kVetor, nVetor = interpretaValores(texto)
		for i in range(T):
			k = kVetor[i]
			n = nVetor[i]
			max, min = calculaResultado(k, n)
			imprimeResultado(i+1, max, min)
		texto = lêEntrada()
			
def calculaResultado(k, n):
	dic = {n:1}
	i = 0
	while True:
		if 2**(i) >= k:
			res = reduz(dic, k)
			k = 0
			break
		dic = reduz(dic)
		k -= 2 ** i
		i += 1
	return encontraMaxMin(res)
		
def reduz(dic, num = None):
	novoDic = {}
	if num is None:
		for ch, val in dic.items():
			if not ch % 2: #ch é par
				parteMaior = int(ch / 2)
				parteMenor = parteMaior - 1
				if not parteMaior in novoDic.keys():
					novoDic[parteMaior] = val
				else:
					novoDic[parteMaior] += val
				if not parteMenor in novoDic.keys():
					novoDic[parteMenor] = val
				else:
					novoDic[parteMenor] += val
			else:
				partes = int((ch - 1) / 2)
				if not partes in novoDic.keys():
					novoDic[partes] = 2 * val
				else:
					novoDic[partes] += 2 * val
		return novoDic
	else:
		while True:
			ch = encontraÓtimo(dic)
			if num > dic[ch]:
				num -= dic[ch]
				del(dic[ch])
			else:
				return ch
				
def encontraÓtimo(dic):
	return max(dic.keys())

def encontraMaxMin(res):
	if res % 2: #ímpar
		return (int((res - 1) / 2), int((res - 1) / 2))
	else: #par
		return (int(res/2), int(res/2 - 1))
		
def lêEntrada():
	try:
		texto = input()
		num = int(texto)
		texto += "\n"
		for i in range(num):
			texto += input() + "\n"
		texto = texto[:-1]
		return texto
	except EOFError:
		return ""
	
def interpretaValores(texto):
	linhas = texto.split("\n")
	T = int(linhas[0])
	kVet, nVet = [], []
	for linha in linhas[1:]:
		nVet.append(int(linha.split()[0]))
		kVet.append(int(linha.split()[1]))
	assert((len(nVet) == T) and (T == len(kVet)))
	return T, kVet, nVet

def imprimeResultado(i, max, min):
	res = "Case #" + str(i) + ": "+ str(max) + " " + str(min)
	print(res)

if __name__ == "__main__":
	cabineFinal()
