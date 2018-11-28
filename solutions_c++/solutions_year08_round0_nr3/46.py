#include <cstdio>
#include <cmath>

const double pi = acos(-1);

double areaCorte(double R, double d) {
	// sendo d < R, qual a menor area obtida pelo corte de um circulo
	// de raio R, sendo que esse corte esta a uma distancia d do centro ?
	
	double areaTotal = pi*R*R;
	double angulo = acos(d/R);
	double areaSecaoCirculo = (areaTotal*angulo)/pi;

	double base = 2*sqrt(R*R - d*d);
	double areaTriangulo = base*d/2;
	
	double retorno = areaSecaoCirculo - areaTriangulo;
	
	//printf(" ** R = %lf , d = %lf -->>   areaTotal = %lf , angulo = %lf , areaSecaoCirculo = %lf , base = %lf, areaTriangulo = %lf , AreaCorte = %lf\n", R, d, areaTotal, angulo, areaSecaoCirculo, base, areaTriangulo, retorno);
	
	return retorno;
}

double process() {

	double f, R, t, r, g;
	scanf("%lf %lf %lf %lf %lf ", &f, &R, &t, &r, &g);

	double resposta;
	
	if (g <= 2*f) {
		// nao tem como a bola de diametro maior que os lados dos quadrados passar por eles
		resposta = 1;
		//printf("foi direto\n");
		
	} else {
	
		double circuloExterno; // area do circulo de raio R
		double Ri; // raio do circulo interno, onde as strings imaginarias passam
		double circuloInterno; // area do circulo de raio R - t - f
		double areaLivre; // area das strings imaginarias que passam pelos quadrados possiveis
		double ladoQuad; // lado do quadrado livre nas string imaginarias
		
		circuloExterno = pi*R*R;
		Ri = R - t - f;
		circuloInterno = pi*Ri*Ri;
		areaLivre = 0;
		ladoQuad = g - 2*f;
		//printf("R = %lf   circuloExterno = %lf   Ri = %lf   areaLivre = %lf\n", R, circuloExterno, Ri, areaLivre);
		
		// d representa a distancia entre o centro da esfera e a string imaginaria analisada
		for (double dx = r + f ; dx < Ri ; dx+= g + 2*r) {
			
			// enquanto um ponto do quadrado estiver dentro do circulo
			for (double dy = r + f ; pow(dy,2) + pow(dx,2) < pow(Ri,2) ; dy += g + 2*r) {
				
				// estou com um quadrado
				
				// sera que o ponto A, na quina oposta do quadrado, esta no circulo?
				
				if (pow(dx+ladoQuad, 2) + pow(dy+ladoQuad, 2) <= pow(Ri, 2)) {
					
					// o quadrado inteiro esta dentro
					areaLivre+= ladoQuad * ladoQuad;
					
				} else {
					
					bool bDentro = pow(dx, 2) + pow(dy+ladoQuad, 2) <= pow(Ri, 2);
					bool cDentro = pow(dx+ladoQuad, 2) + pow(dy, 2) <= pow(Ri, 2);
					
					if (bDentro && cDentro) {
						
						//ambos
						// precisa achar um incremento i para o eixo x, com eq. de segundo grau
						// a = 1;
						double b = 2*dx;
						double c = pow(dx,2) + pow(dy+ladoQuad, 2) - pow(Ri,2);
						double delta = pow(b,2) -4*c;
						
						double i = (sqrt(delta) - b) / 2;
						if (i < 0) i = (1 - sqrt(delta) - b) / 2;
						
						areaLivre+= (areaCorte(Ri, dx+i) - areaCorte(Ri, dx + ladoQuad))/2 - (ladoQuad-i)*dy;
						areaLivre+= ladoQuad*i;
						
					} else if (bDentro) {
						
						// so B

						// a = 1;
						double b = 2*dx;
						double c = pow(dx,2) + pow(dy+ladoQuad, 2) - pow(Ri,2);
						double delta = pow(b,2) -4*c;
						
						double i = (sqrt(delta) - b) / 2;
						if (i < 0) i = (1 - sqrt(delta) - b) / 2;
						
						// a = 1;
						b = 2*dx;
						c = pow(dx,2) + pow(dy, 2) - pow(Ri,2);
						delta = pow(b,2) -4*c;
						
						double j = (sqrt(delta) - b) / 2;
						if (j < 0) j = (1 - sqrt(delta) - b) / 2;
						
						
						
						
						areaLivre+= (areaCorte(Ri, dx+i) - areaCorte(Ri, dx+j))/2 - (j-i)*dy;
						areaLivre+= ladoQuad*i;
						
					} else if (cDentro) {
						
						// so C
						areaLivre+= (areaCorte(Ri, dx) - areaCorte(Ri, dx + ladoQuad))/2 - ladoQuad * dy;
						
					} else {
						
						// nenhum
						// precisa achar um incremento i para o eixo x, com eq. de segundo grau
						// a = 1;
						double b = 2*dx;
						double c = pow(dx,2) + pow(dy, 2) - pow(Ri,2);
						double delta = pow(b,2) -4*c;
						
						double i = (sqrt(delta) - b) / 2;
						if (i < 0) i = (1 - sqrt(delta) - b) / 2;
						areaLivre+= (areaCorte(Ri, dx) - areaCorte(Ri, dx + i))/2 - i*dy;
					}
					
				}
				
				
			}
			
			/*areaLivre+= areaCorte(Ri, dx);
			if (dx + g - 2*f < Ri) {
				areaLivre-= areaCorte(Ri, dx + g - 2*f);
			}*/
		}
		areaLivre = 4 * areaLivre; // so procuramos em um quadrante
		
		

		//double probStringImagin = (areaLivre*areaLivre) / (circuloExterno * circuloInterno);
		double probStringImagin = areaLivre / circuloExterno;
		//printf("areaLivre = %lf    prob = %lf\n", areaLivre, probStringImagin);
		
	
		resposta = 1 - probStringImagin;
		
	}
	
	return resposta;
}

int main() {

	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	int qnt;
	scanf("%d ", &qnt);
	
	for (int i = 1 ; i <= qnt ; i++) {
		printf("Case #%d: %lf\n", i, process());
		
		//printf("\n");
	}
	
	return 0;
}
